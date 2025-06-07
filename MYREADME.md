## Features Added

### Notes CRUD API (`/api/notes`)
- Create Note (POST `/api/notes`)
- Read All Notes (GET `/api/notes`)
- Read One Note (GET `/api/notes/<id>`)
- Update Note (PUT `/api/notes/<id>`)
- Delete Note (DELETE `/api/notes/<id>`)

All responses are in JSON format and use proper status codes and error messages.

## Frontend
- HTML form added inside `templates/pages/placeholder.home.html`
- Dynamically loads notes using JavaScript
- Supports adding, editing, and deleting notes inline

## Unit Tests
- All CRUD operations are tested with `pytest` in `tests/test_notes_api.py`
- Includes both **positive** and **negative** test cases
- Covers edge cases like missing fields, invalid note IDs, and empty content
- Achieves **100% test coverage** for the Notes API