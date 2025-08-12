#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Blueprint, jsonify, request
from models import Note, db_session
from datetime import datetime

#----------------------------------------------------------------------------#
# API Blueprint
#----------------------------------------------------------------------------#
api_bp = Blueprint('api', __name__, url_prefix='/api')

#----------------------------------------------------------------------------#
# Helper Functions
#----------------------------------------------------------------------------#

def validate_note_data(data):
    """Validate note data from request"""
    errors = []
    
    if not data.get('title') or not data.get('title').strip():
        errors.append('Title is required')
    
    if not data.get('content') or not data.get('content').strip():
        errors.append('Content is required')
    
    return errors

#----------------------------------------------------------------------------#
# REST API Endpoints
#----------------------------------------------------------------------------#

# GET /api/notes - Get all notes
@api_bp.route('/notes', methods=['GET'])
def get_notes():
    """
    Get all notes
    
    Query Parameters:
        search: Search term to filter notes
        tag: Filter notes by tag
    
    Returns:
        JSON array of all notes
    """
    try:
        search_term = request.args.get('search')
        tag_filter = request.args.get('tag')
        
        if search_term:
            notes = Note.search_notes(search_term)
        elif tag_filter:
            notes = Note.get_notes_by_tag(tag_filter)
        else:
            notes = Note.get_all_notes()
        
        return jsonify({
            'success': True,
            'data': [note.to_dict() for note in notes],
            'count': len(notes)
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# GET /api/notes/<id> - Get a single note
@api_bp.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    """
    Get a single note by ID
    
    Args:
        note_id: The ID of the note to retrieve
    
    Returns:
        JSON object of the note
    """
    try:
        note = Note.get_note_by_id(note_id)
        
        if not note:
            return jsonify({
                'success': False,
                'error': 'Note not found'
            }), 404
        
        return jsonify({
            'success': True,
            'data': note.to_dict()
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# POST /api/notes - Create a new note
@api_bp.route('/notes', methods=['POST'])
def create_note():
    """
    Create a new note
    
    Request Body:
        title: Note title (required)
        content: Note content (required)
        tags: Comma-separated tags (optional)
    
    Returns:
        JSON object of the created note
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        # Validate data
        errors = validate_note_data(data)
        if errors:
            return jsonify({
                'success': False,
                'errors': errors
            }), 400
        
        # Create note
        note = Note.create_note(
            title=data['title'].strip(),
            content=data['content'].strip(),
            tags=data.get('tags', '').strip() if data.get('tags') else None
        )
        
        return jsonify({
            'success': True,
            'data': note.to_dict(),
            'message': 'Note created successfully'
        }), 201
    
    except Exception as e:
        db_session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# PUT /api/notes/<id> - Update a note
@api_bp.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    """
    Update an existing note
    
    Args:
        note_id: The ID of the note to update
    
    Request Body:
        title: Note title (optional)
        content: Note content (optional)
        tags: Comma-separated tags (optional)
    
    Returns:
        JSON object of the updated note
    """
    try:
        note = Note.get_note_by_id(note_id)
        
        if not note:
            return jsonify({
                'success': False,
                'error': 'Note not found'
            }), 404
        
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        # Update fields if provided
        title = data.get('title')
        content = data.get('content')
        tags = data.get('tags')
        
        # Validate if title or content are provided
        if title is not None and not title.strip():
            return jsonify({
                'success': False,
                'error': 'Title cannot be empty'
            }), 400
            
        if content is not None and not content.strip():
            return jsonify({
                'success': False,
                'error': 'Content cannot be empty'
            }), 400
        
        updated_note = Note.update_note(
            note_id,
            title=title.strip() if title else None,
            content=content.strip() if content else None,
            tags=tags.strip() if tags else None
        )
        
        return jsonify({
            'success': True,
            'data': updated_note.to_dict(),
            'message': 'Note updated successfully'
        }), 200
    
    except Exception as e:
        db_session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# DELETE /api/notes/<id> - Delete a note
@api_bp.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    """
    Delete a note
    
    Args:
        note_id: The ID of the note to delete
    
    Returns:
        Success message
    """
    try:
        note = Note.get_note_by_id(note_id)
        
        if not note:
            return jsonify({
                'success': False,
                'error': 'Note not found'
            }), 404
        
        success = Note.delete_note(note_id)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Note deleted successfully'
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to delete note'
            }), 500
    
    except Exception as e:
        db_session.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# GET /api/tags - Get all unique tags
@api_bp.route('/tags', methods=['GET'])
def get_tags():
    """
    Get all unique tags from all notes
    
    Returns:
        JSON array of unique tags
    """
    try:
        notes = Note.get_all_notes()
        all_tags = set()
        
        for note in notes:
            if note.tags:
                tags = [tag.strip() for tag in note.tags.split(',')]
                all_tags.update(tags)
        
        return jsonify({
            'success': True,
            'data': sorted(list(all_tags))
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

#----------------------------------------------------------------------------#
# Error Handlers
#----------------------------------------------------------------------------#

@api_bp.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@api_bp.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500
