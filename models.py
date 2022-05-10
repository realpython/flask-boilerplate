from flask import abort, Blueprint
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

db = SQLAlchemy()

# DEFINE YOUR MODELS HERE

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def checkPassword(self, entered_password):
        return sha256_crypt.verify(entered_password, self.password)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = sha256_crypt.encrypt(password)
        return None

# FLASK_ADMIN CONFIGURATION
class DefaultModelView(ModelView):
    restricted = True

    def __init__(self, model, session, name=None, category=None, endpoint=None, url=None, **kwargs):
        self.column_default_sort = ('id', True)
        super(DefaultModelView, self).__init__(model, session, name=name, category=category, endpoint=endpoint, url=url)

    def is_accessible(self):
        return current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        abort(401)
# ---------------------------------------------------------------------------- #