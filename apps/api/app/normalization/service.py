from typing import Dict, Any
from app.normalization.schemas import NormalizedEvent
from app.normalization.parsers.generic import GenericParser
from app.normalization.parsers.windows import WindowsParser

class NormalizationService:
    def __init__(self):
        self.parsers = {
            "windows": WindowsParser(),
            "generic": GenericParser()
        }
        self.default_parser = GenericParser()

    def normalize(self, raw_event: Dict[str, Any], source_type: str = "generic") -> NormalizedEvent:
        parser = self.parsers.get(source_type.lower(), self.default_parser)
        return parser.parse(raw_event)
