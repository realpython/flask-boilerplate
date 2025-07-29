from flask import Blueprint, request, jsonify
from .models import Note, Tag, note_tag, Comment
from . import db_session

notes_bp = Blueprint('notes', __name__, url_prefix='/api/notes')
tags_bp = Blueprint('tags', __name__, url_prefix='/api/tags')
comments_bp = Blueprint('comments', __name__, url_prefix='/api/comments')

@notes_bp.route('/', methods=['GET'])
def get_notes():
    notes = db_session.query(Note).all()
    return jsonify([{'id': n.id, 'title': n.title, 'content': n.content} for n in notes])

@notes_bp.route('/', methods=['POST'])
def create_note():
    data = request.json
    new_note = Note(title=data['title'], content=data['content'])
    db_session.add(new_note)
    db_session.commit()
    return jsonify({'message': 'Note created'}), 201

@notes_bp.route('/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.json
    note = db_session.query(Note).get(note_id)
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    note.title = data['title']
    note.content = data['content']
    db_session.commit()
    return jsonify({'message': 'Note updated'})

@notes_bp.route('/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = db_session.query(Note).get(note_id)
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    db_session.delete(note)
    db_session.commit()
    return jsonify({'message': 'Note deleted'})

@tags_bp.route('/', methods=['POST'])
def create_tag():
    data = request.json
    tag = Tag(name=data['name'])
    db_session.add(tag)
    db_session.commit()
    return jsonify({'message': 'Tag created', 'id': tag.id}), 201

@tags_bp.route('/', methods=['GET'])
def get_tags():
    tags = db_session.query(Tag).all()
    return jsonify([{'id': t.id, 'name': t.name} for t in tags])

@tags_bp.route('/<int:tag_id>', methods=['PUT'])
def update_tag(tag_id):
    data = request.json
    tag = db_session.query(Tag).get(tag_id)
    if not tag:
        return jsonify({'error': 'Tag not found'}), 404
    tag.name = data['name']
    db_session.commit()
    return jsonify({'message': 'Tag updated'})

@tags_bp.route('/<int:tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    tag = db_session.query(Tag).get(tag_id)
    if not tag:
        return jsonify({'error': 'Tag not found'}), 404
    db_session.delete(tag)
    db_session.commit()
    return jsonify({'message': 'Tag deleted'})

@comments_bp.route('/', methods=['POST'])
def create_comment():
    data = request.json
    comment = Comment(content=data['content'], post_id=data['post_id'])
    db_session.add(comment)
    db_session.commit()
    return jsonify({'message': 'Comment created', 'id': comment.id}), 201

@comments_bp.route('/', methods=['GET'])
def get_comments():
    post_id = request.args.get('post_id')
    query = db_session.query(Comment)
    if post_id:
        query = query.filter_by(post_id=post_id)
    comments = query.all()
    return jsonify([
        {'id': c.id, 'content': c.content, 'post_id': c.post_id, 'created_at': c.created_at.isoformat()}
        for c in comments
    ])

@comments_bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    data = request.json
    comment = db_session.query(Comment).get(comment_id)
    if not comment:
        return jsonify({'error': 'Comment not found'}), 404
    comment.content = data['content']
    db_session.commit()
    return jsonify({'message': 'Comment updated'})

@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = db_session.query(Comment).get(comment_id)
    if not comment:
        return jsonify({'error': 'Comment not found'}), 404
    db_session.delete(comment)
    db_session.commit()
    return jsonify({'message': 'Comment deleted'})
