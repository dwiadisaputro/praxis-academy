from operator import truediv
import my_app
import unittest

class MyTestCase(unittest.TestCase):
    
    def MyTestCase(unittest.TestCase):
        my_app.app.testing = true
        self.app = my_app.app.test_client()
        
    def test_home(self):
        result = self.app.get('/')
        #Make your assertions