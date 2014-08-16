import json
import unittest

from app import create_app


class TestClient(object):
    def __init__(self, app):
        self.app = app

    def send(self, url, method, data=None, headers=None):
        if headers is None:
            headers = {}
        if data:
            data = json.dumps(data)
        with self.app.test_request_context(url, method=method, data=data,
                                           headers=headers):
            rv = self.app.preprocess_request()
            if rv is None:
                rv = self.app.dispatch_request()
            rv = self.app.make_response(rv)
            rv = self.app.process_response(rv)
            return rv

    def get(self, url, headers=None):
        return self.send(url, 'GET', headers=headers)

    def post(self, url, data, headers=None):
        return self.send(url, 'POST', data, headers=headers)

    def put(self, url, data, headers={}):
        return self.send(url, 'PUT', data, headers=headers)

    def delete(self, url, headers={}):
        return self.send(url, 'DELETE', headers=headers)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config')
        self.ctx = self.app.app_context()
        self.ctx.push()
        self.client = TestClient(self.app)

    def tearDown(self):
        self.ctx.pop()
