from typing import Dict, Any
from datetime import datetime
from app.normalization.base import BaseParser
from app.normalization.schemas import NormalizedEvent, EventType, EventAction

class GenericParser(BaseParser):
    def parse(self, raw_event: Dict[str, Any]) -> NormalizedEvent:
        # Determine timestamp
        timestamp = self._extract_alias(raw_event, ["timestamp", "time", "date"])
        if isinstance(timestamp, str):
            try:
                timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            except ValueError:
                raise ValueError(f"Invalid timestamp format: {timestamp}")
        elif not isinstance(timestamp, datetime):
             raise ValueError(f"Missing or invalid timestamp")

        # Map types and actions gracefully
        event_type_str = str(self._extract_alias(raw_event, ["event_type", "type"]) or "unknown")
        try:
            event_type = EventType(event_type_str)
        except ValueError:
            event_type = EventType.unknown

        action_str = str(self._extract_alias(raw_event, ["action", "event_action"]) or "unknown")
        try:
            action = EventAction(action_str)
        except ValueError:
            action = EventAction.unknown

        return NormalizedEvent(
            event_id=str(self._extract_alias(raw_event, ["event_id", "id"])) if self._extract_alias(raw_event, ["event_id", "id"]) else None,
            timestamp=timestamp,
            source=str(self._extract_alias(raw_event, ["source", "log_source"]) or "generic"),
            source_type=str(self._extract_alias(raw_event, ["source_type"])) if self._extract_alias(raw_event, ["source_type"]) else None,
            event_type=event_type,
            action=action,
            username=str(self._extract_alias(raw_event, ["user", "username", "AccountName"])) if self._extract_alias(raw_event, ["user", "username", "AccountName"]) else None,
            source_ip=str(self._extract_alias(raw_event, ["src_ip", "source_ip", "IpAddress"])) if self._extract_alias(raw_event, ["src_ip", "source_ip", "IpAddress"]) else None,
            destination_ip=str(self._extract_alias(raw_event, ["dst_ip", "destination_ip"])) if self._extract_alias(raw_event, ["dst_ip", "destination_ip"]) else None,
            hostname=str(self._extract_alias(raw_event, ["host", "hostname", "ComputerName"])) if self._extract_alias(raw_event, ["host", "hostname", "ComputerName"]) else None,
            process=str(self._extract_alias(raw_event, ["process", "process_name"])) if self._extract_alias(raw_event, ["process", "process_name"]) else None,
            command_line=str(self._extract_alias(raw_event, ["cmd", "command_line", "CommandLine"])) if self._extract_alias(raw_event, ["cmd", "command_line", "CommandLine"]) else None,
            status=str(self._extract_alias(raw_event, ["status"])) if self._extract_alias(raw_event, ["status"]) else None,
            raw_event=raw_event
        )
