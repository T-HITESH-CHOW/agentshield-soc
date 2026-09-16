import os

# Schemas
schemas_dir = 'apps/api/app/schemas'
os.makedirs(schemas_dir, exist_ok=True)

with open(f'{schemas_dir}/__init__.py', 'w') as f:
    pass

with open(f'{schemas_dir}/alert.py', 'w', encoding='utf-8') as f:
    f.write('''from pydantic import BaseModel, ConfigDict, Field
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
''')

# API Router
api_dir = 'apps/api/app/api/v1'

with open(f'{api_dir}/alerts.py', 'w', encoding='utf-8') as f:
    f.write('''from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from datetime import datetime, timezone

from app.db.session import get_db
from app.db.models.alert import Alert, AlertStatus
from app.schemas.alert import AlertCreate, AlertUpdate, AlertResponse

router = APIRouter()

@router.post("/alerts", response_model=AlertResponse, status_code=201)
def create_alert(alert_in: AlertCreate, db: Session = Depends(get_db)):
    alert_data = alert_in.model_dump(exclude_unset=True)
    if "status" not in alert_data:
        alert_data["status"] = AlertStatus.NEW
    
    db_alert = Alert(**alert_data)
    # Set default dates for testing purposes when there is no real DB
    now = datetime.now(timezone.utc)
    if not hasattr(db_alert, "created_at") or not db_alert.created_at:
        db_alert.created_at = now
    if not hasattr(db_alert, "updated_at") or not db_alert.updated_at:
        db_alert.updated_at = now
        
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

@router.get("/alerts", response_model=List[AlertResponse])
def list_alerts(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    alerts = db.query(Alert).offset(skip).limit(limit).all()
    return alerts

@router.get("/alerts/{alert_id}", response_model=AlertResponse)
def get_alert(alert_id: UUID, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert

@router.patch("/alerts/{alert_id}", response_model=AlertResponse)
def update_alert(alert_id: UUID, alert_in: AlertUpdate, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    
    update_data = alert_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(alert, field, value)
    
    db.commit()
    db.refresh(alert)
    return alert
''')

# Update v1 router
with open(f'{api_dir}/__init__.py', 'w', encoding='utf-8') as f:
    f.write('''"""Versioned API surface."""
from fastapi import APIRouter
from app.api.v1.alerts import router as alerts_router

router = APIRouter(prefix="/api/v1")
router.include_router(alerts_router, tags=["Alerts"])
''')

# Tests
tests_dir = 'apps/api/tests'
with open(f'{tests_dir}/test_api_alerts.py', 'w', encoding='utf-8') as f:
    f.write('''from fastapi.testclient import TestClient
from app.main import app
from app.db.session import get_db
import uuid
from datetime import datetime, timezone
from unittest.mock import MagicMock

# Create a mock database session
mock_db = MagicMock()

# Store fake data here
fake_db_storage = {}

def get_mock_db():
    yield mock_db

# Override dependency
app.dependency_overrides[get_db] = get_mock_db

client = TestClient(app)

class MockQuery:
    def __init__(self, items):
        self.items = items
    
    def offset(self, skip):
        return MockQuery(self.items[skip:])
        
    def limit(self, limit):
        return MockQuery(self.items[:limit])
        
    def all(self):
        return self.items
        
    def filter(self, condition):
        # Extremely basic mock filter just for id == alert_id
        # We assume the condition is basically Alert.id == value
        # In a real mock we'd evaluate the expression, here we just return matching ID from fake_db_storage
        # Since we can't easily parse the SQLAlchemy binary expression without a real engine,
        # we just grab the single item from storage if it exists (assuming tests only ask for valid/invalid ids).
        # We will cheat a bit by letting the tests set what `filter` returns via mock_db.query(Alert).filter.return_value
        pass

def setup_function():
    mock_db.reset_mock()
    fake_db_storage.clear()

def mock_add(obj):
    if not hasattr(obj, "id") or obj.id is None:
        obj.id = uuid.uuid4()
    fake_db_storage[obj.id] = obj

def mock_commit():
    pass

def mock_refresh(obj):
    pass

mock_db.add.side_effect = mock_add
mock_db.commit.side_effect = mock_commit
mock_db.refresh.side_effect = mock_refresh


def test_post_valid_alert():
    data = {
        "title": "Suspicious Login",
        "severity": "HIGH",
        "source": "Wazuh",
        "detected_at": "2026-09-16T10:00:00Z",
        "raw_event": {"user": "admin"}
    }
    response = client.post("/api/v1/alerts", json=data)
    assert response.status_code == 201
    res_data = response.json()
    assert res_data["title"] == "Suspicious Login"
    assert res_data["status"] == "NEW"
    assert "id" in res_data

def test_post_missing_title():
    data = {
        "severity": "HIGH",
        "source": "Wazuh",
        "detected_at": "2026-09-16T10:00:00Z"
    }
    response = client.post("/api/v1/alerts", json=data)
    assert response.status_code == 422

def test_post_missing_source():
    data = {
        "title": "Suspicious Login",
        "severity": "HIGH",
        "detected_at": "2026-09-16T10:00:00Z"
    }
    response = client.post("/api/v1/alerts", json=data)
    assert response.status_code == 422

def test_post_invalid_severity():
    data = {
        "title": "Suspicious Login",
        "severity": "INVALID_SEV",
        "source": "Wazuh",
        "detected_at": "2026-09-16T10:00:00Z"
    }
    response = client.post("/api/v1/alerts", json=data)
    assert response.status_code == 422

def test_get_list_alerts():
    # Setup mock query
    class MQ:
        def offset(self, n): return self
        def limit(self, n): return self
        def all(self): return []
    mock_db.query.return_value = MQ()
    
    response = client.get("/api/v1/alerts")
    assert response.status_code == 200
    assert response.json() == []

def test_get_by_id_returns_correct_alert():
    alert_id = uuid.uuid4()
    
    class MQ:
        def filter(self, cond):
            class M:
                def first(self):
                    from app.db.models.alert import Alert, AlertSeverity, AlertStatus
                    a = Alert(title="Mocked", source="Test", severity=AlertSeverity.HIGH, detected_at=datetime.now(timezone.utc))
                    a.id = alert_id
                    a.status = AlertStatus.NEW
                    a.created_at = datetime.now(timezone.utc)
                    a.updated_at = datetime.now(timezone.utc)
                    return a
            return M()
            
    mock_db.query.return_value = MQ()
    response = client.get(f"/api/v1/alerts/{alert_id}")
    assert response.status_code == 200
    assert response.json()["id"] == str(alert_id)
    assert response.json()["title"] == "Mocked"

def test_get_by_nonexistent_id():
    class MQ:
        def filter(self, cond):
            class M:
                def first(self): return None
            return M()
            
    mock_db.query.return_value = MQ()
    response = client.get(f"/api/v1/alerts/{uuid.uuid4()}")
    assert response.status_code == 404

def test_patch_change_status():
    alert_id = uuid.uuid4()
    from app.db.models.alert import Alert, AlertSeverity, AlertStatus
    a = Alert(title="Mocked", source="Test", severity=AlertSeverity.HIGH, detected_at=datetime.now(timezone.utc))
    a.id = alert_id
    a.status = AlertStatus.NEW
    a.created_at = datetime.now(timezone.utc)
    a.updated_at = datetime.now(timezone.utc)
    
    class MQ:
        def filter(self, cond):
            class M:
                def first(self): return a
            return M()
            
    mock_db.query.return_value = MQ()
    
    patch_data = {"status": "RESOLVED"}
    response = client.patch(f"/api/v1/alerts/{alert_id}", json=patch_data)
    assert response.status_code == 200
    assert response.json()["status"] == "RESOLVED"

def test_patch_invalid_status():
    alert_id = uuid.uuid4()
    patch_data = {"status": "INVALID_STATUS"}
    response = client.patch(f"/api/v1/alerts/{alert_id}", json=patch_data)
    assert response.status_code == 422
''')
