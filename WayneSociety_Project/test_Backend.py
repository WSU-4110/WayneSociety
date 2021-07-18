from werkzeug.wrappers.response import Response
from Deploy import app, db, User
import unittest
from flask import abort, url_for
from flask_testing import TestCase



class TestBackendFunctions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # Testing for Welcome Page Routing
    def test_welcome_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Wayne Society', response.data)


   # Testing for Login Page Routing
    def test_Login_page(self):
        response = self.app.get('/Login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login into your account to view all categories', response.data)
        self.assertIn(b'Welcome Back :)', response.data)


    # Testing for Signup Page Routing
    def test_Signup_page(self):
        response = self.app.get('/Signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Join WayneSociety Today', response.data)


    #Testing for Jobs Page Routing
    def test_Jobs_page(self):
        response = self.app.get('/Jobs')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jobs', response.data)


    #Testing for Attractions Page Routing
    def test_Attractions_page(self):
        response = self.app.get('/Attractions')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Attractions', response.data)

        

    # Testing for Service Page Routing
    def test_Services_page(self):
        response = self.app.get('/Services')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Services', response.data)

    
    # Testing for Events Page Routing
    def test_Events_page(self):
        response = self.app.get('/Events')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Find tickets', response.data)


    # Testing for Food Page Routing
    def test_Food_page(self):
        response = self.app.get('/Food')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Foods', response.data)


    # Testing for About Us Page Routing
    def test_AboutUs_page(self):
        response = self.app.get('/AboutUs')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Meet Our Developers', response.data)

        
    

    
        




if __name__ == '__main__':
    unittest_Main()


