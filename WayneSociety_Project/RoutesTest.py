import unittest


#from Deploy.py import app
from Deploy import app


# class unittest.TestCases
class RoutesTest(unittest.TestCase):
    """
    This class contains all of the tests for the Routes class
    """

    def setUp(self):
        """
        This function sets up the tests
        """
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False


    def test_homepage(self):
        """
        This function tests the homepage
        """
        result = self.app.get('/', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Welcome to the Wayne Society', result.data)
        self.assertIn('<title>Welcome to the Wayne Society</title>', result.data)
        self.assertIn('<h1>Welcome to the Wayne Society</h1>', result.data)
        

    def test_about(self):
        """
        This function tests the about page
        """
        result = self.app.get('/About', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn('About the Wayne Society', result.data)
        self.assertIn('<title>About the Wayne Society</title>', result.data)
        self.assertIn('<h1>About the Wayne Society</h1>', result.data)

    def test_events(self):
        """
        This function tests the events page
        """
        result = self.app.get('/Events', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Events', result.data)
        self.assertIn('<title>Events</title>', result.data)
        self.assertIn('<h1>Events</h1>', result.data)

    def test_attractions(self):
        """
        This function tests the attractions page
        """
        result = self.app.get('/Attractions', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Attractions', result.data)
        self.assertIn('<title>Attractions</title>', result.data)
        self.assertIn('<h1>Attractions</h1>', result.data)

    def test_food(self):
        """
        This function tests the food page
        """
        result = self.app.get('/Food', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Food', result.data)
        self.assertIn('<title>Food</title>', result.data)
        self.assertIn('<h1>Food</h1>', result.data)

    

    def test_home(self):
        """
        This function tests the home page
        """
        result = self.app.get('/Home', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Home', result.data)
        self.assertIn('<title>Home</title>', result.data)
        self.assertIn('<h1>Home</h1>', result.data)

    
    def test_login(self):
        """
        This function tests the login page
        """
        result = self.app.get('/Login', follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Login', result.data)
        self.assertIn('<title>Login</title>', result.data)
        self.assertIn('<h1>Login</h1>', result.data)


    def test_get_login_up(self):
        """
        This function tests the login page
        """
        result = self.app.get('/Login', methods=['POST'], follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Login', result.data)
        self.assertIn('<title>Login</title>', result.data)
        self.assertIn('<h1>Login</h1>', result.data)


if __name__ == '__main__':
    unittest.main()