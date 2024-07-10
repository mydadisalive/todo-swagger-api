import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_todo():
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Buy groceries"

def test_create_todo():
    new_todo = {"id": 3, "title": "Exercise", "description": "Run 5km", "completed": False}
    response = client.post("/todos", json=new_todo)
    assert response.status_code == 200
    assert response.json() == new_todo

def test_update_todo():
    updated_todo = {"id": 1, "title": "Buy groceries", "description": "Milk, Bread, Cheese, Eggs", "completed": False}
    response = client.put("/todos/1", json=updated_todo)
    assert response.status_code == 200
    assert response.json() == updated_todo

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Buy groceries"
