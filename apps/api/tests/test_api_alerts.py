from fastapi.testclient import TestClient
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
