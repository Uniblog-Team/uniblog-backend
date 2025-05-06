# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app  # Importa tu instancia de FastAPI


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de UniBlog está funcionando"}
