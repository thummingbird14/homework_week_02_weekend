import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Tanya",50.00)
        
    def test_guest_has_name(self):
        self.assertEqual("Tanya", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest.wallet)