import os

DEBUG = True

HOST = 'localhost'
PORT = int(os.environ.get('PORT', 5000))
SERVER_NAME = '{}:{}'.format(HOST, PORT)
