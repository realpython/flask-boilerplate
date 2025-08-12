# Note-Taking Flask Application

A comprehensive note-taking web application built with Flask, featuring full CRUD operations and REST API endpoints.

## Features

### Core Features
- **Create, Read, Update, Delete (CRUD)** operations for notes
- **Tagging system** for organizing notes
- **Search functionality** across titles and content
- **RESTful API** with full CRUD endpoints
- **Responsive web interface**
- **SQLite database** for data persistence

### API Endpoints

#### Notes API
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/notes` | Get all notes (supports search and tag filtering) |
| GET | `/api/notes/<id>` | Get a specific note by ID |
| POST | `/api/notes` | Create a new note |
| PUT | `/api/notes/<id>` | Update an existing note |
| DELETE | `/api/notes/<id>` | Delete a note |

#### Tags API
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tags` | Get all unique tags |

### Note Structure
```json
{
  "id": 1,
  "title": "My Note Title",
  "content": "Note content goes here...",
  "tags": "work,important,flask",
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T14:45:00"
}
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd note-taking_flask_app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   python -c "from models import Base, engine; Base.metadata.create_all(bind=engine)"
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

## Usage

### Web Interface
- Visit `http://localhost:5000` to access the web interface
- Use the navigation to access different pages

### API Usage Examples

#### Create a new note
```bash
curl -X POST http://localhost:5000/api/notes \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Note",
    "content": "This is the content of my first note",
    "tags": "personal,important"
  }'
```

#### Get all notes
```bash
curl http://localhost:5000/api/notes
```

#### Search notes
```bash
curl "http://localhost:5000/api/notes?search=flask"
```

#### Get notes by tag
```bash
curl "http://localhost:5000/api/notes?tag=work"
```

#### Update a note
```bash
curl -X PUT http://localhost:5000/api/notes/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Note Title",
    "content": "Updated content"
  }'
```

#### Delete a note
```bash
curl -X DELETE http://localhost:5000/api/notes/1
```

## Database Schema

### Notes Table
- `id` (INTEGER, PRIMARY KEY)
- `title` (VARCHAR(200), NOT NULL)
- `content` (TEXT, NOT NULL)
- `tags` (VARCHAR(500), NULLABLE)
- `created_at` (DATETIME, DEFAULT: current timestamp)
- `updated_at` (DATETIME, DEFAULT: current timestamp, ON UPDATE: current timestamp)

## Development

### Project Structure
```
note-taking_flask_app/
├── app.py                 # Main application file
├── api.py                 # REST API endpoints
├── models.py              # Database models
├── forms.py               # WTForms definitions
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── database.db            # SQLite database (created on first run)
├── README.md             # This file
├── templates/            # HTML templates
├── static/               # CSS, JS, and image files
└── error.log            # Application logs
```

### Adding New Features
1. Update the database model in `models.py`
2. Add corresponding API endpoints in `api.py`
3. Update the web interface in `app.py`
4. Add appropriate tests

### Testing
The application includes basic error handling and validation. For comprehensive testing:
- Test all CRUD operations via API
- Verify tag filtering and search functionality
- Check error handling for invalid inputs
- Test database transactions

## Deployment

### Using Heroku
1. Create a Heroku app
2. Set environment variables
3. Deploy using Git

### Using Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License
This project is open source and available under the [MIT License](LICENSE).
