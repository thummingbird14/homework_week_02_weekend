import unittest
from classes.room import Room
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room(1,5)
        self.guest_1 = Guest("Tanya")
        self.guest_2 = Guest("Cordii")
           
    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.number)
    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room_1.capacity)

    def test_can_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.assertEqual(2, self.room_1.guest_count())

    def test_can_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_out_guest(self.guest_1)
        self.assertEqual(1, self.room_1.guest_count())    