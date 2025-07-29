from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def create_app():
    app = Flask(__name__)

    from .routes import notes_bp, tags_bp, comments_bp
    app.register_blueprint(notes_bp)
    app.register_blueprint(tags_bp)
    app.register_blueprint(comments_bp)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    Base.metadata.create_all(bind=engine)
    return app
