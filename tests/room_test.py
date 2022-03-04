import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room(1,5)
        self.guest_1 = Guest("Tanya")
        self.guest_2 = Guest("Cordii")
        self.guest_3 = Guest("Stephanie")
        self.guest_4 = Guest("Eli")
        self.guest_5 = Guest("Kevin")
        self.guest_6 = Guest("Annika")
        self.song_1 = Song("I Will Survive")
           
    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.number)
    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room_1.capacity)

    def test_check_in_guest_has_capacity(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.assertEqual(2, self.room_1.guest_count())

    def test_check_in_guest_no_capacity(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_in_guest(self.guest_4)
        self.room_1.check_in_guest(self.guest_5)
        self.room_1.check_in_guest(self.guest_6)
        self.assertEqual(5, self.room_1.guest_count())

    def test_can_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_out_guest(self.guest_1)
        self.assertEqual(1, self.room_1.guest_count())

    def test_can_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1,self.room_1.song_count())