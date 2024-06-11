class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    def add_to_genre_count(self):
        if self.genre in self.__class__.genre_count:
            self.__class__.genre_count[self.genre] += 1
        else:
            self.__class__.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in self.__class__.artist_count:
            self.__class__.artist_count[self.artist] += 1
        else:
            self.__class__.artist_count[self.artist] = 1
