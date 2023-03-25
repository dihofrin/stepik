"""
https://stepik.org/lesson/674263/step/15?unit=672698

Функция max_pair()
Реализуйте функцию max_pair(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются числа
Функция должна возвращать единственное число — максимальную сумму двух соседних чисел итерируемого объекта iterable.
"""

from itertools import pairwise

def max_pair(iterable):
    pairs = pairwise(iterable)
    return sum(max(pairs, key=sum))

