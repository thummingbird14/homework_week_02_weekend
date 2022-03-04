import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room(1,15)
           
    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)
    
    def test_room_has_capacity(self):
        self.assertEqual(15, self.room.capacity)    