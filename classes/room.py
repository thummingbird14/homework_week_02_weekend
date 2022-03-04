class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = []
        self.songs = []

    def guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            guest.wallet -= 10.00

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def song_count(self):
        return len(self.songs)

    def add_song(self, song):
        self.songs.append(song)