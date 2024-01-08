from abc import ABC, abstractmethod
from collections.abc import Iterable, Container
from Validator_descriptors import Date


class Genre(ABC):
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __repr__(self):
        return f'{self.__name} music'


class Artist:
    date = Date('date')

    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __repr__(self):
        return f'{self.name}'


class Album:
    release_date = Date('release_date')

    def __init__(self, title: str, artist: Artist, release_date: str):
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.__songs = []

    @property
    def songs(self):
        return self.__songs

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, value):
        self.__artist = value

    def __contains__(self, song):
        if song in self.songs:
            return True

    def __repr__(self):
        return f'{self.title}'


class Song:
    def __init__(self, title: str, artist: Artist, album: Album, length: str, genre: Genre):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.genre = genre
        self.album.songs.append(self)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, value):
        self.__artist = value

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, value):
        self.__album = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    def __repr__(self):
        return f'{self.title}'


class Playlist(Iterable, Container):
    def __init__(self, name: str):
        self.name = name
        self.__songs = []
        self.index = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def songs(self):
        return self.__songs

    def __contains__(self, song):
        if song in self.songs:
            return True

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.songs):
            self.value = self.songs[self.index]
            self.index += 1
            return self.value
        else:
            raise StopIteration

    def next(self):
        return self.__next__()

    def add_song(self, song: Song):
        self.__songs.append(song)

    def add_album(self, album: Album):
        self.__songs.extend(album.songs)

    def __repr__(self):
        return f'{self.name}'


class Player:
    def __init__(self):
        self.__history = []

    @property
    def history(self):
        return self.__history

    @staticmethod
    def search(song: Song, playlist: Playlist):
        if song in playlist:
            print(f'The song is N {playlist.songs.index(song)} on the playlist.')
        else:
            print('Song not found')

    def stream(self, song, playlist: Playlist):
        if song in playlist:
            print(f'{song.title} is playing.')
            self.__history.append(song)

    def next(self, playlist: Playlist):
        return playlist.next()



if __name__ == '__main__':
    print('___________________________________________________________')
    print('Creating a genre.')

    rock = Genre('rock')
    print(rock)

    print('___________________________________________________________')
    print('Creating an artist.')

    pink_floyd = Artist('Pink Floyd', '01.01.1965')
    print(pink_floyd)

    print('___________________________________________________________')
    print('Creating albums.')

    dark_side = Album('Dark Side of the Moon', pink_floyd, '01.03.1973')
    wish_you = Album('Wish You Were Here', pink_floyd, '01.01.1975')
    the_wall = Album('The Wall', pink_floyd, '01.01.1979')

    print('Album: ', dark_side)
    print('Album: ', wish_you)
    print('Album: ', the_wall)

    print('___________________________________________________________')
    print('Creating songs.')

    breathe = Song('Breathe', pink_floyd, dark_side, '3:58', rock)
    time = Song('Time', pink_floyd, dark_side, '7:06', rock)
    money = Song('Money', pink_floyd, dark_side, '6:22', rock)
    shine = Song('Shine On You Crazy Diamond', pink_floyd, wish_you, '13:31', rock)
    you_were_here = Song('Wish You Were Here', pink_floyd, wish_you, '5:34', rock)
    cigar = Song('Have a Cigar', pink_floyd, wish_you, '5:08', rock)
    brick_wall = Song('Another Brick in the Wall', pink_floyd, the_wall, '3:59', rock)
    numb = Song('Comfortably Numb', pink_floyd, the_wall, '6:24', rock)
    hey_you = Song('Hey You', pink_floyd, the_wall, '4:40', rock)

    print('The songs should be in the albums.')
    print(dark_side.songs)
    print(wish_you.songs)
    print(the_wall.songs)

    print('___________________________________________________________')
    print('Creating a playlist and adding songs.')

    my_playlist = Playlist('My Playlist')
    my_playlist.add_song(breathe)
    my_playlist.add_album(the_wall)
    print(my_playlist)

    print('___________________________________________________________')
    print('Here are the songs in the playlist')

    print(my_playlist.songs)

    print('___________________________________________________________')
    print('Creating a player.')

    player = Player()
    print(player)

    print('___________________________________________________________')
    print('Checking the behavior.')
    print('___________________________________________________________')
    print('Streaming a song.')
    player.stream(breathe, my_playlist)
    player.stream(brick_wall, my_playlist)
    player.stream(numb, my_playlist)

    print('___________________________________________________________')
    print('Viewing the history.')
    print(player.history)

    print('___________________________________________________________')
    print('Searching a song')
    player.search(you_were_here, my_playlist)
    player.search(hey_you, my_playlist)
    print(shine in my_playlist)
    print(player.next(my_playlist))
    print(player.next(my_playlist))
    print(player.next(my_playlist))
    print(player.next(my_playlist))



    


