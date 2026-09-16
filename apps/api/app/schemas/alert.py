from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Dict, Any
from datetime import datetime
import uuid
from app.db.models.alert import AlertSeverity, AlertStatus

class AlertBase(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    severity: AlertSeverity
    source: str = Field(..., min_length=1)
    source_type: Optional[str] = None
    detected_at: datetime
    source_ip: Optional[str] = None
    destination_ip: Optional[str] = None
    hostname: Optional[str] = None
    username: Optional[str] = None
    detection_rule: Optional[str] = None
    mitre_technique: Optional[str] = None
    raw_event: Optional[Dict[str, Any]] = None

class AlertCreate(AlertBase):
    external_id: Optional[str] = None
    status: Optional[AlertStatus] = None

class AlertUpdate(BaseModel):
    status: Optional[AlertStatus] = None
    severity: Optional[AlertSeverity] = None

class AlertResponse(AlertBase):
    id: uuid.UUID
    external_id: Optional[str] = None
    status: AlertStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
