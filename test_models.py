#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import pytest
import os
import tempfile
from datetime import datetime
from models import Note, db_session, engine, Base
from sqlalchemy import create_engine

#----------------------------------------------------------------------------#
# Test Setup
#----------------------------------------------------------------------------#

@pytest.fixture
def test_db():
    """Create a test database for each test"""
    # Create temporary database
    test_engine = create_engine('sqlite:///:memory:', echo=False)
    Base.metadata.create_all(bind=test_engine)
    
    # Override the session
    from sqlalchemy.orm import scoped_session, sessionmaker
    test_session = scoped_session(sessionmaker(bind=test_engine))
    Note.query = test_session.query_property()
    
    yield test_session
    
    # Cleanup
    test_session.close()
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture
def sample_note_data():
    """Sample note data for testing"""
    return {
        'title': 'Test Note',
        'content': 'This is a test note content',
        'tags': 'test,important,work'
    }

#----------------------------------------------------------------------------#
# Model Tests
#----------------------------------------------------------------------------#

class TestNoteModel:
    """Test cases for Note model"""
    
    def test_create_note(self, test_db):
        """Test creating a new note"""
        note = Note.create_note(
            title='Test Note',
            content='Test content',
            tags='test,work'
        )
        
        assert note.id is not None
        assert note.title == 'Test Note'
        assert note.content == 'Test content'
        assert note.tags == 'test,work'
        assert isinstance(note.created_at, datetime)
        assert isinstance(note.updated_at, datetime)
    
    def test_create_note_without_tags(self, test_db):
        """Test creating a note without tags"""
        note = Note.create_note(
            title='No Tags Note',
            content='Content without tags'
        )
        
        assert note.id is not None
        assert note.title == 'No Tags Note'
        assert note.content == 'Content without tags'
        assert note.tags is None
    
    def test_get_all_notes(self, test_db):
        """Test retrieving all notes"""
        # Create test notes
        Note.create_note('Note 1', 'Content 1', 'tag1')
        Note.create_note('Note 2', 'Content 2', 'tag2')
        
        notes = Note.get_all_notes()
        
        assert len(notes) == 2
        assert notes[0].title == 'Note 2'  # Should be ordered by created_at desc
        assert notes[1].title == 'Note 1'
    
    def test_get_note_by_id(self, test_db):
        """Test retrieving a note by ID"""
        note = Note.create_note('Test Note', 'Test content')
        retrieved_note = Note.get_note_by_id(note.id)
        
        assert retrieved_note is not None
        assert retrieved_note.id == note.id
        assert retrieved_note.title == 'Test Note'
    
    def test_get_note_by_nonexistent_id(self, test_db):
        """Test retrieving a non-existent note"""
        note = Note.get_note_by_id(999)
        assert note is None
    
    def test_update_note(self, test_db):
        """Test updating a note"""
        note = Note.create_note('Original Title', 'Original content', 'original')
        
        updated_note = Note.update_note(
            note.id,
            title='Updated Title',
            content='Updated content',
            tags='updated,new'
        )
        
        assert updated_note is not None
        assert updated_note.title == 'Updated Title'
        assert updated_note.content == 'Updated content'
        assert updated_note.tags == 'updated,new'
        assert updated_note.updated_at > updated_note.created_at
    
    def test_update_note_partial(self, test_db):
        """Test partial update of a note"""
        note = Note.create_note('Title', 'Content', 'tags')
        
        updated_note = Note.update_note(
            note.id,
            title='New Title Only'
        )
        
        assert updated_note.title == 'New Title Only'
        assert updated_note.content == 'Content'  # Should remain unchanged
        assert updated_note.tags == 'tags'  # Should remain unchanged
    
    def test_update_nonexistent_note(self, test_db):
        """Test updating a non-existent note"""
        updated_note = Note.update_note(999, title='New Title')
        assert updated_note is None
    
    def test_delete_note(self, test_db):
        """Test deleting a note"""
        note = Note.create_note('To Delete', 'Content to delete')
        
        success = Note.delete_note(note.id)
        assert success is True
        
        deleted_note = Note.get_note_by_id(note.id)
        assert deleted_note is None
    
    def test_delete_nonexistent_note(self, test_db):
        """Test deleting a non-existent note"""
        success = Note.delete_note(999)
        assert success is False
    
    def test_search_notes(self, test_db):
        """Test searching notes"""
        Note.create_note('Python Note', 'This is about Python programming')
        Note.create_note('JavaScript Note', 'This is about JavaScript')
        Note.create_note('Flask Note', 'This is about Flask framework')
        
        results = Note.search_notes('Python')
        assert len(results) == 1
        assert results[0].title == 'Python Note'
        
        results = Note.search_notes('programming')
        assert len(results) == 1
        assert results[0].title == 'Python Note'
    
    def test_search_notes_no_results(self, test_db):
        """Test searching notes with no matches"""
        Note.create_note('Note 1', 'Content 1')
        
        results = Note.search_notes('nonexistent')
        assert len(results) == 0
    
    def test_get_notes_by_tag(self, test_db):
        """Test getting notes by tag"""
        Note.create_note('Work Note', 'Work content', 'work,important')
        Note.create_note('Personal Note', 'Personal content', 'personal,important')
        Note.create_note('Other Note', 'Other content', 'other')
        
        results = Note.get_notes_by_tag('important')
        assert len(results) == 2
        
        results = Note.get_notes_by_tag('work')
        assert len(results) == 1
        assert results[0].title == 'Work Note'
    
    def test_get_notes_by_nonexistent_tag(self, test_db):
        """Test getting notes by non-existent tag"""
        Note.create_note('Note 1', 'Content 1', 'tag1')
        
        results = Note.get_notes_by_tag('nonexistent')
        assert len(results) == 0
    
    def test_to_dict(self, test_db):
        """Test note serialization to dictionary"""
        note = Note.create_note('Test Note', 'Test content', 'test,tag')
        
        note_dict = note.to_dict()
        
        assert isinstance(note_dict, dict)
        assert note_dict['id'] == note.id
        assert note_dict['title'] == 'Test Note'
        assert note_dict['content'] == 'Test content'
        assert note_dict['tags'] == 'test,tag'
        assert 'created_at' in note_dict
        assert 'updated_at' in note_dict
        assert isinstance(note_dict['created_at'], str)
        assert isinstance(note_dict['updated_at'], str)
    
    def test_repr(self, test_db):
        """Test string representation of note"""
        note = Note.create_note('Test Note', 'Content')
        assert repr(note) == '<Note Test Note>'
