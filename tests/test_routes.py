from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login():
    response = client.post("/token", data={"username": "user", "password": "!3Ba92753$"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_user_route():
    token = client.post("/token", data={"username": "user", "password": "!3Ba92753$"}).json()["access_token"]
    response = client.get("/user", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome, user!"}

def test_admin_route():
    token = client.post("/token", data={"username": "admin", "password": "admin!3Ba92753$"}).json()["access_token"]
    response = client.get("/admin", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome, admin!"}
