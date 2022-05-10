import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# https://randomkeygen.com/
# Use `CodeIgniter Encryption Keys - Can be used for any other 256-bit key requirement.`
SECRET_KEY = 'dFt5FnCZxYiiEFnbeZdRsXS9UhkLaHq3'

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False