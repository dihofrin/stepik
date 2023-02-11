"""
https://stepik.org/lesson/640045/step/17?unit=636565

Функция alnum_sequence()
Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.

Функция должна возвращать итератор, циклично генерирующий бесконечную последовательность натуральных чисел и заглавных латинских букв:
"""

from itertools import count, cycle
from string import ascii_uppercase
chars = (char for obj in zip(count(1), ascii_uppercase) for char in obj)
def alnum_sequence():
    yield from cycle(chars)
