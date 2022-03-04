import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("I Will Survive")
        
        
    def test_song_has_title(self):
        self.assertEqual("I Will Survive", self.song.title)