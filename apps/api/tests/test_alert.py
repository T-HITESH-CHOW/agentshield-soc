import pytest
import uuid
from datetime import datetime, timezone
from app.db.models.alert import Alert, AlertSeverity, AlertStatus
from app.db.base import Base

def test_alert_instantiation():
    now = datetime.now(timezone.utc)
    alert = Alert(
        title="Test Alert",
        severity=AlertSeverity.HIGH,
        source="Test Source",
        detected_at=now,
    )
    
    assert alert.title == "Test Alert"
    assert alert.severity == AlertSeverity.HIGH
    assert alert.source == "Test Source"
    assert alert.detected_at == now
    assert Alert.__table__.c.status.default.arg == AlertStatus.NEW
    
def test_alert_severity_enum():
    assert AlertSeverity.LOW == "LOW"
    assert AlertSeverity.MEDIUM == "MEDIUM"
    assert AlertSeverity.HIGH == "HIGH"
    assert AlertSeverity.CRITICAL == "CRITICAL"
    
def test_alert_status_enum():
    assert AlertStatus.NEW == "NEW"
    assert AlertStatus.ACKNOWLEDGED == "ACKNOWLEDGED"
    assert AlertStatus.INVESTIGATING == "INVESTIGATING"
    assert AlertStatus.RESOLVED == "RESOLVED"
    assert AlertStatus.FALSE_POSITIVE == "FALSE_POSITIVE"

def test_alert_raw_event():
    raw = {"key": "value", "nested": {"foo": "bar"}}
    now = datetime.now(timezone.utc)
    alert = Alert(
        title="Test JSON",
        severity=AlertSeverity.LOW,
        source="Test Source",
        detected_at=now,
        raw_event=raw
    )
    assert alert.raw_event["key"] == "value"
    assert alert.raw_event["nested"]["foo"] == "bar"

def test_alert_registered_in_metadata():
    assert "alerts" in Base.metadata.tables
    table = Base.metadata.tables["alerts"]
    assert table.name == "alerts"
    assert "id" in table.c
    assert "title" in table.c
    assert "severity" in table.c
    assert "status" in table.c
    assert "raw_event" in table.c

import os
def test_alembic_migration_exists():
    versions_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "alembic", "versions")
    files = os.listdir(versions_dir)
    migration_files = [f for f in files if f.endswith(".py") and f != "__init__.py"]
    assert len(migration_files) >= 1
    
    # Check if any migration references the alerts table
    found_alerts_table = False
    for filename in migration_files:
        with open(os.path.join(versions_dir, filename), "r") as f:
            content = f.read()
            if "create_table(\n        'alerts'" in content or "create_table('alerts'" in content:
                found_alerts_table = True
                break
    
    assert found_alerts_table, "No migration file creates the 'alerts' table"
