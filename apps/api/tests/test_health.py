from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["service"] == "agentshield-api"
