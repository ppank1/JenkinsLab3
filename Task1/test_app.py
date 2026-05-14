import unittest
import os
from app import app

class TestHomeRoute(unittest.TestCase):
    """Unit tests for the Flask application home route."""

    def setUp(self):
        """Set up test client before each test."""
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_status_code(self):
        """Test that the home route returns a 200 status code."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_contains_hello(self):
        """Test that the response contains 'Hello'."""
        response = self.client.get('/')
        self.assertIn(b'Hello', response.data)

    def test_home_default_name(self):
        """Test that the default name 'friend' is used when YOUR_NAME is not set."""
        os.environ.pop('YOUR_NAME', None)
        response = self.client.get('/')
        self.assertIn(b'friend', response.data)

    def test_home_custom_name(self):
        """Test that a custom name is displayed when YOUR_NAME env var is set."""
        os.environ['YOUR_NAME'] = 'TestUser'
        response = self.client.get('/')
        self.assertIn(b'TestUser', response.data)
        os.environ.pop('YOUR_NAME', None)

    def test_home_contains_hostname(self):
        """Test that the response contains hostname info."""
        response = self.client.get('/')
        self.assertIn(b"I'm currently running in", response.data)

    def test_home_returns_html(self):
        """Test that the response content type is HTML."""
        response = self.client.get('/')
        self.assertIn('text/html', response.content_type)

    def test_invalid_route_returns_404(self):
        """Test that an invalid route returns a 404 status code."""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_home_method_not_allowed(self):
        """Test that POST to home route returns 405 Method Not Allowed."""
        response = self.client.post('/')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
