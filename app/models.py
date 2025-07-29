from . import Base
from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

note_tag = Table(
    'note_tag', Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text)
    tags = relationship('Tag', secondary=note_tag, back_populates='notes')

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    notes = relationship('Note', secondary=note_tag, back_populates='tags')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey('notes.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    note = relationship('Note', backref='comments')
