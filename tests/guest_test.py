import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Tanya")
        
        
    def test_guest_has_name(self):
        self.assertEqual("Tanya", self.guest.name)