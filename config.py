import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# enable debug mode
DEBUG = True

# secret key for session management
SECRET_KEY = 'my precious'

# connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
