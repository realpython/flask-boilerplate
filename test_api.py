#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import pytest
import json
from app import app
from models import Note, db_session, Base, engine
from datetime import datetime

#----------------------------------------------------------------------------#
# Test Setup
#----------------------------------------------------------------------------#

@pytest.fixture
def client():
    """Create a test client"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            # Create tables
            Base.metadata.create_all(bind=engine)
            yield client
            # Cleanup
            Base.metadata.drop_all(bind=engine)

@pytest.fixture
def sample_note():
    """Create a sample note for testing"""
    note = Note.create_note(
        title='Test Note',
        content='This is test content',
        tags='test,api'
    )
    return note

#----------------------------------------------------------------------------#
# API Tests
#----------------------------------------------------------------------------#

class TestNotesAPI:
    """Test cases for Notes API endpoints"""
    
    def test_get_all_notes_empty(self, client):
        """Test getting all notes when none exist"""
        response = client.get('/api/notes')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['data'] == []
        assert data['count'] == 0
    
    def test_get_all_notes_with_data(self, client):
        """Test getting all notes with existing data"""
        # Create test notes
        Note.create_note('Note 1', 'Content 1', 'tag1')
        Note.create_note('Note 2', 'Content 2', 'tag2')
        
        response = client.get('/api/notes')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert len(data['data']) == 2
        assert data['count'] == 2
    
    def test_get_note_by_id(self, client, sample_note):
        """Test getting a specific note by ID"""
        response = client.get(f'/api/notes/{sample_note.id}')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['data']['id'] == sample_note.id
        assert data['data']['title'] == 'Test Note'
    
    def test_get_note_by_nonexistent_id(self, client):
        """Test getting a non-existent note"""
        response = client.get('/api/notes/999')
        data = json.loads(response.data)
        
        assert response.status_code == 404
        assert data['success'] is False
        assert data['error'] == 'Note not found'
    
    def test_create_note_success(self, client):
        """Test creating a new note successfully"""
        note_data = {
            'title': 'New Note',
            'content': 'New content',
            'tags': 'new,test'
        }
        
        response = client.post('/api/notes',
                             data=json.dumps(note_data),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 201
        assert data['success'] is True
        assert data['data']['title'] == 'New Note'
        assert data['data']['content'] == 'New content'
        assert data['data']['tags'] == 'new,test'
        assert 'id' in data['data']
    
    def test_create_note_missing_title(self, client):
        """Test creating a note without title"""
        note_data = {
            'content': 'Content without title',
            'tags': 'test'
        }
        
        response = client.post('/api/notes',
                             data=json.dumps(note_data),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert data['success'] is False
        assert 'errors' in data
        assert 'Title is required' in data['errors']
    
    def test_create_note_missing_content(self, client):
        """Test creating a note without content"""
        note_data = {
            'title': 'Title without content',
            'tags': 'test'
        }
        
        response = client.post('/api/notes',
                             data=json.dumps(note_data),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert data['success'] is False
        assert 'errors' in data
        assert 'Content is required' in data['errors']
    
    def test_create_note_empty_json(self, client):
        """Test creating a note with empty JSON"""
        response = client.post('/api/notes',
                             data=json.dumps({}),
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert data['success'] is False
        assert data['error'] == 'No data provided'
    
    def test_create_note_invalid_json(self, client):
        """Test creating a note with invalid JSON"""
        response = client.post('/api/notes',
                             data='invalid json',
                             content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 400
    
    def test_update_note_success(self, client, sample_note):
        """Test updating a note successfully"""
        update_data = {
            'title': 'Updated Title',
            'content': 'Updated content',
            'tags': 'updated,new'
        }
        
        response = client.put(f'/api/notes/{sample_note.id}',
                            data=json.dumps(update_data),
                            content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['data']['title'] == 'Updated Title'
        assert data['data']['content'] == 'Updated content'
        assert data['data']['tags'] == 'updated,new'
    
    def test_update_note_partial(self, client, sample_note):
        """Test partial update of a note"""
        update_data = {
            'title': 'Only Title Updated'
        }
        
        response = client.put(f'/api/notes/{sample_note.id}',
                            data=json.dumps(update_data),
                            content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['data']['title'] == 'Only Title Updated'
        assert data['data']['content'] == 'This is test content'  # Should remain unchanged
    
    def test_update_note_empty_title(self, client, sample_note):
        """Test updating a note with empty title"""
        update_data = {
            'title': '',
            'content': 'Updated content'
        }
        
        response = client.put(f'/api/notes/{sample_note.id}',
                            data=json.dumps(update_data),
                            content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert data['success'] is False
        assert data['error'] == 'Title cannot be empty'
    
    def test_update_nonexistent_note(self, client):
        """Test updating a non-existent note"""
        update_data = {
            'title': 'Updated Title',
            'content': 'Updated content'
        }
        
        response = client.put('/api/notes/999',
                            data=json.dumps(update_data),
                            content_type='application/json')
        data = json.loads(response.data)
        
        assert response.status_code == 404
        assert data['success'] is False
        assert data['error'] == 'Note not found'
    
    def test_delete_note_success(self, client, sample_note):
        """Test deleting a note successfully"""
        response = client.delete(f'/api/notes/{sample_note.id}')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['message'] == 'Note deleted successfully'
        
        # Verify note is actually deleted
        response = client.get(f'/api/notes/{sample_note.id}')
        assert response.status_code == 404
    
    def test_delete_nonexistent_note(self, client):
        """Test deleting a non-existent note"""
        response = client.delete('/api/notes/999')
        data = json.loads(response.data)
        
        assert response.status_code == 404
        assert data['success'] is False
        assert data['error'] == 'Note not found'
    
    def test_search_notes(self, client):
        """Test searching notes"""
        Note.create_note('Python Programming', 'Learn Python basics', 'python,programming')
        Note.create_note('JavaScript Guide', 'JavaScript tutorial', 'javascript,programming')
        Note.create_note('Flask Framework', 'Flask web development', 'flask,python')
        
        response = client.get('/api/notes?search=python')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert len(data['data']) == 2  # Should find both Python-related notes
    
    def test_search_notes_no_results(self, client):
        """Test searching notes with no matches"""
        Note.create_note('Note 1', 'Content 1')
        
        response = client.get('/api/notes?search=nonexistent')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert len(data['data']) == 0
    
    def test_get_notes_by_tag(self, client):
        """Test filtering notes by tag"""
        Note.create_note('Work Note', 'Work content', 'work,important')
        Note.create_note('Personal Note', 'Personal content', 'personal,important')
        Note.create_note('Other Note', 'Other content', 'other')
        
        response = client.get('/api/notes?tag=important')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert len(data['data']) == 2
    
    def test_get_notes_by_nonexistent_tag(self, client):
        """Test filtering notes by non-existent tag"""
        Note.create_note('Note 1', 'Content 1', 'tag1')
        
        response = client.get('/api/notes?tag=nonexistent')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert len(data['data']) == 0
    
    def test_get_all_tags(self, client):
        """Test getting all unique tags"""
        Note.create_note('Note 1', 'Content 1', 'work,important')
        Note.create_note('Note 2', 'Content 2', 'personal,important')
        Note.create_note('Note 3', 'Content 3', 'work,urgent')
        
        response = client.get('/api/tags')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert 'important' in data['data']
        assert 'work' in data['data']
        assert 'personal' in data['data']
        assert 'urgent' in data['data']
        assert len(data['data']) == 4
    
    def test_get_all_tags_empty(self, client):
        """Test getting tags when no notes exist"""
        response = client.get('/api/tags')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['data'] == []
    
    def test_get_all_tags_no_tags(self, client):
        """Test getting tags when notes have no tags"""
        Note.create_note('Note 1', 'Content 1')
        Note.create_note('Note 2', 'Content 2')
        
        response = client.get('/api/tags')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data['success'] is True
        assert data['data'] == []
    
    def test_api_404_endpoint(self, client):
        """Test 404 error for non-existent API endpoint"""
        response = client.get('/api/nonexistent')
        data = json.loads(response.data)
        
        assert response.status_code == 404
        assert data['success'] is False
        assert data['error'] == 'Endpoint not found'
