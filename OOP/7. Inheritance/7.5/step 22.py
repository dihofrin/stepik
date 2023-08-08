"""
https://stepik.org/lesson/872533/step/22?unit=876917

Функции is_iterator() и is_iterable()
1. Реализуйте функцию is_iterable(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.

2. Также реализуйте функцию is_iterator(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итератором, или False в противном случае.
"""

from collections.abc import Iterable, Iterator

def is_iterator(obj):
    return isinstance(obj, Iterator)

def is_iterable(obj):
    return isinstance(obj, Iterable)