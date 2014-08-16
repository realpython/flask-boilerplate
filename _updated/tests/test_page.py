from .helpers import TestCase


class TestPage(TestCase):
    def test_header(self):
        rv = self.client.get('/')
        assert "Hello world!" in rv.data
