import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room(1,5)
        self.guest_1 = Guest("Tanya", 50.00)
        self.guest_2 = Guest("Cordii", 40.00)
        self.guest_3 = Guest("Stephanie", 60.00)
        self.guest_4 = Guest("Eli", 65.50)
        self.guest_5 = Guest("Kevin", 55.00)
        self.guest_6 = Guest("Annika", 58.50)
        self.song_1 = Song("I Will Survive")
           
    def test_room_has_number(self):
        self.assertEqual(1, self.room_1.number)
    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room_1.capacity)

    def test_check_in_guest_has_capacity(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.assertEqual(2, self.room_1.guest_count())

    def test_wallet_decremented_on_check_in(self):
        self.room_1.check_in_guest(self.guest_3)
        self.assertEqual(50.00,self.guest_3.wallet)

    def test_check_in_guest_no_capacity(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.room_1.check_in_guest(self.guest_4)
        self.room_1.check_in_guest(self.guest_5)
        self.room_1.check_in_guest(self.guest_6)
        self.assertEqual(5, self.room_1.guest_count())
        self.assertEqual(58.50, self.guest_6.wallet)

    def test_can_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_out_guest(self.guest_1)
        self.assertEqual(1, self.room_1.guest_count())

    def test_can_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1,self.room_1.song_count())