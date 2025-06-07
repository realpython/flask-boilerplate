from flask import Blueprint, request, jsonify
from models import Note, db_session

notes_bp = Blueprint('notes', __name__, url_prefix='/api/notes')

@notes_bp.route('', methods=['POST'])
def create_note():
    """
    Create a new note
    ---
    tags:
      - Notes
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - title
            properties:
              title:
                type: string
              content:
                type: string
    responses:
      201:
        description: Note created successfully
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Note'
      400:
        description: Missing required field
    """
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    note = Note(title=data['title'], content=data.get('content'))
    db_session.add(note)
    db_session.commit()
    return jsonify(note.to_dict()), 201

@notes_bp.route('', methods=['GET'])
def get_notes():
    notes = db_session.query(Note).all()
    return jsonify([note.to_dict() for note in notes]), 200

@notes_bp.route('/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = db_session.query(Note).get(note_id)
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    return jsonify(note.to_dict()), 200

@notes_bp.route('/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = db_session.query(Note).get(note_id)
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    data = request.get_json()
    note.title = data.get('title', note.title)
    note.content = data.get('content', note.content)
    db_session.commit()
    return jsonify(note.to_dict()), 200

@notes_bp.route('/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = db_session.query(Note).get(note_id)
    if not note:
        return jsonify({'error': 'Note not found'}), 404
    db_session.delete(note)
    db_session.commit()
    return jsonify({'message': 'Note deleted'}), 200
