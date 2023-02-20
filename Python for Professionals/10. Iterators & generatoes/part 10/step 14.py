"""
https://stepik.org/lesson/674263/step/14?unit=672698

  Функция is_rising()
Реализуйте функцию is_rising(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются числа
Функция должна возвращать True, если элементы итерируемого объекта расположены строго по возрастанию, или False в противном случае.
"""

from itertools import pairwise
def is_rising(iterable):
    prices = pairwise(iterable)
    return all((price[1] > price[0]) for price in prices)

