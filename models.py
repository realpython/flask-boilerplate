#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

#----------------------------------------------------------------------------#
# Database Setup
#----------------------------------------------------------------------------#
engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

#----------------------------------------------------------------------------#
# Models
#----------------------------------------------------------------------------#

class Note(Base):
    """
    Note Model
    Represents a note in the note-taking application
    
    Attributes:
        id (int): Primary key
        title (str): Note title
        content (str): Note content/body
        tags (str): Comma-separated tags for categorization
        created_at (datetime): Creation timestamp
        updated_at (datetime): Last update timestamp
    """
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    tags = Column(String(500), nullable=True)  # Comma-separated tags
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Note {self.title}>'
    
    def to_dict(self):
        """Convert note object to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @classmethod
    def create_note(cls, title, content, tags=None):
        """Create a new note"""
        note = cls(title=title, content=content, tags=tags)
        db_session.add(note)
        db_session.commit()
        return note
    
    @classmethod
    def get_all_notes(cls):
        """Get all notes ordered by creation date (newest first)"""
        return cls.query.order_by(cls.created_at.desc()).all()
    
    @classmethod
    def get_note_by_id(cls, note_id):
        """Get a single note by ID"""
        return cls.query.get(note_id)
    
    @classmethod
    def update_note(cls, note_id, title=None, content=None, tags=None):
        """Update an existing note"""
        note = cls.get_note_by_id(note_id)
        if note:
            if title is not None:
                note.title = title
            if content is not None:
                note.content = content
            if tags is not None:
                note.tags = tags
            note.updated_at = datetime.utcnow()
            db_session.commit()
            return note
        return None
    
    @classmethod
    def delete_note(cls, note_id):
        """Delete a note by ID"""
        note = cls.get_note_by_id(note_id)
        if note:
            db_session.delete(note)
            db_session.commit()
            return True
        return False
    
    @classmethod
    def search_notes(cls, search_term):
        """Search notes by title or content"""
        search_pattern = f"%{search_term}%"
        return cls.query.filter(
            cls.title.ilike(search_pattern) | cls.content.ilike(search_pattern)
        ).order_by(cls.created_at.desc()).all()
    
    @classmethod
    def get_notes_by_tag(cls, tag):
        """Get all notes with a specific tag"""
        tag_pattern = f"%{tag}%"
        return cls.query.filter(cls.tags.ilike(tag_pattern)).order_by(cls.created_at.desc()).all()

# Create tables
Base.metadata.create_all(bind=engine)
