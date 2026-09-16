from enum import Enum
from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field

class EventType(str, Enum):
    authentication = "authentication"
    network = "network"
    process = "process"
    file = "file"
    dns = "dns"
    system = "system"
    unknown = "unknown"

class EventAction(str, Enum):
    login_failed = "login_failed"
    login_success = "login_success"
    connection_attempt = "connection_attempt"
    process_start = "process_start"
    file_create = "file_create"
    file_modify = "file_modify"
    query = "query"
    unknown = "unknown"

class NormalizedEvent(BaseModel):
    event_id: Optional[str] = None
    timestamp: datetime
    source: str
    source_type: Optional[str] = None
    event_type: EventType = EventType.unknown
    action: EventAction = EventAction.unknown
    username: Optional[str] = None
    source_ip: Optional[str] = None
    destination_ip: Optional[str] = None
    hostname: Optional[str] = None
    process: Optional[str] = None
    command_line: Optional[str] = None
    status: Optional[str] = None
    raw_event: Dict[str, Any]
