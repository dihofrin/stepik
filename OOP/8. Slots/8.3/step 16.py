"""
https://stepik.org/lesson/958398/step/16?unit=964840

Классы MovieGenres и Movie
1. Реализуйте класс MovieGenres, описывающий флаг с жанрами кино. Флаг должен иметь пять элементов:

ACTION
COMEDY
DRAMA
FANTASY
HORROR
2. Также реализуйте класс Movie, описывающий фильм. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — название фильма
genres — жанр фильма (элемент флага MovieGenres)
Класс Movie должен иметь один метод экземпляра:

in_genre() — метод, принимающий в качестве аргумента жанр и возвращающий True, если фильм принадлежит данному жанру, или False в противном случае
Экземпляр класса Movie должен иметь следующее неформальное строковое представление:

<название фильма>
"""

from enum import Flag, auto

class MovieGenres(Flag):

    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()

class Movie:
    def __init__(self, name, genres):
        self.name = name
        self.genres = genres

    def in_genre(self, genre):
        return genre in self.genres

    def __str__(self):
        return self.name

