import pytest
from datetime import datetime, timezone
from app.normalization.service import NormalizationService
from app.normalization.schemas import EventType, EventAction

def test_generic_event_normalization():
    svc = NormalizationService()
    raw = {
        "timestamp": "2026-09-16T10:00:00Z",
        "source": "firewall",
        "event_type": "network",
        "action": "connection_attempt",
        "src_ip": "1.2.3.4"
    }
    event = svc.normalize(raw, "generic")
    assert event.source == "firewall"
    assert event.event_type == EventType.network
    assert event.action == EventAction.connection_attempt
    assert event.source_ip == "1.2.3.4"
    assert event.raw_event == raw

def test_windows_event_4625_failed_login():
    svc = NormalizationService()
    raw = {
        "timestamp": "2026-09-16T10:00:00+00:00",
        "EventID": 4625,
        "AccountName": "admin",
        "IpAddress": "192.168.1.100"
    }
    event = svc.normalize(raw, "windows")
    assert event.event_type == EventType.authentication
    assert event.action == EventAction.login_failed
    assert event.username == "admin"
    assert event.source_ip == "192.168.1.100"
    assert event.raw_event == raw # strictly unchanged

def test_windows_event_4624_successful_login():
    svc = NormalizationService()
    raw = {
        "timestamp": "2026-09-16T10:00:00+00:00",
        "EventID": 4624,
        "AccountName": "user1"
    }
    event = svc.normalize(raw, "windows")
    assert event.event_type == EventType.authentication
    assert event.action == EventAction.login_success
    assert event.username == "user1"
    assert event.raw_event == raw

def test_username_alias_mapping():
    svc = NormalizationService()
    for alias in ["user", "username", "AccountName"]:
        raw = {"timestamp": "2026-09-16T10:00:00Z", alias: "test_user"}
        event = svc.normalize(raw, "generic")
        assert event.username == "test_user"

def test_source_ip_alias_mapping():
    svc = NormalizationService()
    for alias in ["src_ip", "source_ip", "IpAddress"]:
        raw = {"timestamp": "2026-09-16T10:00:00Z", alias: "10.0.0.1"}
        event = svc.normalize(raw, "generic")
        assert event.source_ip == "10.0.0.1"

def test_hostname_alias_mapping():
    svc = NormalizationService()
    for alias in ["host", "hostname", "ComputerName"]:
        raw = {"timestamp": "2026-09-16T10:00:00Z", alias: "server-01"}
        event = svc.normalize(raw, "generic")
        assert event.hostname == "server-01"

def test_missing_optional_fields_become_none():
    svc = NormalizationService()
    raw = {"timestamp": "2026-09-16T10:00:00Z", "source": "test"}
    event = svc.normalize(raw)
    assert event.username is None
    assert event.source_ip is None
    assert event.process is None
    assert event.command_line is None

def test_invalid_timestamp_is_rejected():
    svc = NormalizationService()
    raw = {"timestamp": "not-a-timestamp"}
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        svc.normalize(raw)

def test_unknown_event_type_handled_safely():
    svc = NormalizationService()
    raw = {"timestamp": "2026-09-16T10:00:00Z", "event_type": "some_weird_type", "action": "magic"}
    event = svc.normalize(raw)
    assert event.event_type == EventType.unknown
    assert event.action == EventAction.unknown

def test_raw_event_is_preserved_unchanged():
    svc = NormalizationService()
    raw = {"timestamp": "2026-09-16T10:00:00Z", "secret": "dont-touch", "nested": {"a": 1}}
    event = svc.normalize(raw)
    assert event.raw_event == raw
    assert event.raw_event["secret"] == "dont-touch"

def test_malicious_looking_text_treated_as_data():
    svc = NormalizationService()
    malicious_str = "'; DROP TABLE alerts; --"
    raw = {"timestamp": "2026-09-16T10:00:00Z", "username": malicious_str}
    event = svc.normalize(raw)
    # The string should be preserved exactly without execution or evaluation
    assert event.username == malicious_str
    
def test_no_llm_or_provider_is_called():
    import sys
    assert "openai" not in sys.modules
    assert "anthropic" not in sys.modules
    assert "google.generativeai" not in sys.modules

def test_no_shell_command_executed(monkeypatch):
    import os
    import subprocess
    
    def fake_system(*args, **kwargs):
        raise RuntimeError("Shell execution is forbidden!")
    
    monkeypatch.setattr(os, "system", fake_system)
    monkeypatch.setattr(subprocess, "run", fake_system)
    monkeypatch.setattr(subprocess, "Popen", fake_system)
    
    svc = NormalizationService()
    raw = {"timestamp": "2026-09-16T10:00:00Z", "process": "os.system('id')"}
    event = svc.normalize(raw)
    assert event.process == "os.system('id')"
