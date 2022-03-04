import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room(1,15)
        self.guest_1 = Guest("Tanya")
           
    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)
    
    def test_room_has_capacity(self):
        self.assertEqual(15, self.room.capacity)

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())