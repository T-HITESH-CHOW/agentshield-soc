import enum
import uuid
from datetime import datetime, timezone
from typing import Optional, Any
from sqlalchemy import String, Enum, DateTime, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class AlertSeverity(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class AlertStatus(str, enum.Enum):
    NEW = "NEW"
    ACKNOWLEDGED = "ACKNOWLEDGED"
    INVESTIGATING = "INVESTIGATING"
    RESOLVED = "RESOLVED"
    FALSE_POSITIVE = "FALSE_POSITIVE"

class Alert(Base):
    __tablename__ = "alerts"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    external_id: Mapped[Optional[str]] = mapped_column(String(255), index=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    
    severity: Mapped[AlertSeverity] = mapped_column(Enum(AlertSeverity, native_enum=False, length=50), index=True)
    status: Mapped[AlertStatus] = mapped_column(Enum(AlertStatus, native_enum=False, length=50), default=AlertStatus.NEW, index=True)
    
    source: Mapped[str] = mapped_column(String(255), index=True)
    source_type: Mapped[Optional[str]] = mapped_column(String(255))
    
    detected_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    source_ip: Mapped[Optional[str]] = mapped_column(String(50), index=True)
    destination_ip: Mapped[Optional[str]] = mapped_column(String(50))
    hostname: Mapped[Optional[str]] = mapped_column(String(255), index=True)
    username: Mapped[Optional[str]] = mapped_column(String(255))
    
    detection_rule: Mapped[Optional[str]] = mapped_column(String(255))
    mitre_technique: Mapped[Optional[str]] = mapped_column(String(50))
    
    raw_event: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON)
