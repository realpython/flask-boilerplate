import pytest
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app()

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory DB for tests
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_post_note(client):
    payload = {"title": "Test Note", "content": "This is a test note."}
    response = client.post("/api/notes/", data=json.dumps(payload), content_type="application/json")
    assert response.status_code == 201
    assert b'Note created' in response.data

def test_get_notes(client):
    client.post("/api/notes/", data=json.dumps({"title": "Temp", "content": "Temp"}), content_type="application/json")
    response = client.get("/api/notes/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_update_note(client):
    client.post("/api/notes/", data=json.dumps({"title": "Temp", "content": "Temp"}), content_type="application/json")
    response = client.put("/api/notes/1", data=json.dumps({"title": "Updated", "content": "Updated"}), content_type="application/json")
    assert response.status_code == 200
    assert b'Note updated' in response.data

def test_delete_note(client):
    client.post("/api/notes/", data=json.dumps({"title": "Temp", "content": "Temp"}), content_type="application/json")
    response = client.delete("/api/notes/1")
    assert response.status_code == 200
    assert b'Note deleted' in response.data
