from typing import Dict, Any
from app.normalization.base import BaseParser
from app.normalization.schemas import NormalizedEvent, EventType, EventAction
from app.normalization.parsers.generic import GenericParser

class WindowsParser(BaseParser):
    def __init__(self):
        self.generic_parser = GenericParser()

    def parse(self, raw_event: Dict[str, Any]) -> NormalizedEvent:
        # Pre-process windows specific mappings before passing to generic
        processed_event = dict(raw_event)
        
        event_id = str(self._extract_alias(processed_event, ["EventID", "event_id"]))
        if event_id == "4624":
            processed_event["event_type"] = EventType.authentication.value
            processed_event["action"] = EventAction.login_success.value
        elif event_id == "4625":
            processed_event["event_type"] = EventType.authentication.value
            processed_event["action"] = EventAction.login_failed.value

        processed_event["source"] = processed_event.get("source", "windows")
        
        # Generic parser handles the aliases for AccountName, IpAddress, ComputerName etc.
        # But we pass the ORIGINAL raw event as raw_event inside GenericParser using a trick or just update raw_event manually
        norm_event = self.generic_parser.parse(processed_event)
        norm_event.raw_event = raw_event # restore original pristine raw_event
        return norm_event
