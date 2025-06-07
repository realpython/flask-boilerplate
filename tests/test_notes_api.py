import pytest
import json
from app import app  
from models import Base, engine, db_session, Note


@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    # Use in-memory SQLite DB for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    # Create tables before tests
    Base.metadata.create_all(bind=engine)

    with app.test_client() as client:
        yield client

    # Cleanup after tests
    db_session.remove()
    Base.metadata.drop_all(bind=engine)


def test_create_note_success(test_client):
    response = test_client.post('/api/notes',
        data=json.dumps({'title': 'Test Note', 'content': 'Test Content'}),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == 'Test Note'
    assert data['content'] == 'Test Content'


def test_create_note_fail_no_title(test_client):
    response = test_client.post('/api/notes',
        data=json.dumps({'content': 'No title'}),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data


def test_get_notes(test_client):
    response = test_client.get('/api/notes')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)


def test_get_note_success(test_client):
    # Insert note directly
    note = Note(title='Sample', content='Sample content')
    db_session.add(note)
    db_session.commit()

    response = test_client.get(f'/api/notes/{note.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'Sample'
    assert data['content'] == 'Sample content'


def test_get_note_fail_not_found(test_client):
    response = test_client.get('/api/notes/9999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data


def test_update_note_success(test_client):
    note = Note(title='Old title', content='Old content')
    db_session.add(note)
    db_session.commit()

    response = test_client.put(f'/api/notes/{note.id}',
        data=json.dumps({'title': 'New title', 'content': 'New content'}),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['title'] == 'New title'
    assert data['content'] == 'New content'


def test_update_note_fail_not_found(test_client):
    response = test_client.put('/api/notes/9999',
        data=json.dumps({'title': 'Title'}),
        content_type='application/json'
    )
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data


def test_delete_note_success(test_client):
    note = Note(title='Delete me', content='Delete content')
    db_session.add(note)
    db_session.commit()

    response = test_client.delete(f'/api/notes/{note.id}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data


def test_delete_note_fail_not_found(test_client):
    response = test_client.delete('/api/notes/9999')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data
