from abc import ABC, abstractmethod
from typing import Dict, Any
from app.normalization.schemas import NormalizedEvent

class BaseParser(ABC):
    @abstractmethod
    def parse(self, raw_event: Dict[str, Any]) -> NormalizedEvent:
        pass
        
    def _extract_alias(self, event: Dict[str, Any], aliases: list[str]) -> Any:
        for alias in aliases:
            if alias in event and event[alias] is not None:
                return event[alias]
        return None
