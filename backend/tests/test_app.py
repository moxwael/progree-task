import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["application"] == "cloud-native-api"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_info_endpoint():
    client = app.test_client()
    response = client.get("/api/info")

    assert response.status_code == 200
    assert response.json["version"] == "1.0.0"
