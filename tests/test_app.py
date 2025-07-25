import unittest
import sys
import os

# Add the parent directory to the path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class DashboardTestCase(unittest.TestCase):
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_login_page_loads(self):
        """Test that login page loads successfully"""
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Login', response.data)
    
    def test_redirect_to_login_when_not_authenticated(self):
        """Test that unauthenticated users are redirected to login"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # Redirect
    
    def test_login_with_valid_credentials(self):
        """Test login with valid credentials"""
        response = self.app.post('/login', data={
            'username': 'admin',
            'password': 'password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard Overview', response.data)
    
    def test_login_with_invalid_credentials(self):
        """Test login with invalid credentials"""
        response = self.app.post('/login', data={
            'username': 'wrong',
            'password': 'wrong'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid credentials', response.data)
    
    def test_api_chart_data_without_auth(self):
        """Test that API endpoint requires authentication"""
        response = self.app.get('/api/chart-data')
        self.assertEqual(response.status_code, 401)
    
    def test_logout(self):
        """Test logout functionality"""
        # First login
        with self.app.session_transaction() as sess:
            sess['logged_in'] = True
            sess['username'] = 'admin'
        
        # Then logout
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Login', response.data)

if __name__ == '__main__':
    unittest.main()
