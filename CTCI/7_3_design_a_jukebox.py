"""
Design a Jukebox
"""

class Jukebox(object):
    """
    Jukebox is a platform to play a song
    attributes: collection of songs
    methods:
    play_song(): play a song selected by a user
    stop_song(): stop currently playing song
    """
    def __init__(self, songs):
        self.songs = {}
        for song in songs:
            self.songs[song.title] = song
        self.current_playing = None

    def play_song(self, title):
        if self.current_playing:
            self.stop_song()
        self.current_playing = self.songs[title]
        self.current_playing.play()

    def stop_song(self):
        if self.current_playing:
            self.current_playing.stop()


class Song(object):
    """
    Song consist of attributes > song title and song data.
    Song has methods as:
    play() -> to play a song
    stop() -> to stop a song
    """
    def __init__(self, title, data):
        self.title = title
        self.data = data
        self.play_count = 0
        self.is_playing = None

    def play(self):
        self.is_playing = True
        self.play_count += 1

    def stop(self):
        self.is_playing = False


import unittest

class Test(unittest.TestCase):
    def test_jukebox(self):
        song1 = Song("Just Dance", "1234567")
        song2 = Song("When you wish upon a beard", "987654321")
        jukebox = Jukebox(song1, song2)
        jukebox.play_song("Just Dance")
        self.assertEqual(song1,play_count, 1)



# Ref: https://github.com/w-hat/ctci-solutions/blob/master/ch-07-object-oriented-design/03-jukebox.py