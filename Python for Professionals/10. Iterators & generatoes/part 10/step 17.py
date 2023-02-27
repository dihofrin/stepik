"""
https://stepik.org/lesson/674263/step/17?unit=672698

Функция grouper()
Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность, элементами которой являются объединенные в кортежи по n элементов соседние элементы итерируемого объекта iterable. Если у элемента не достаточно соседей, то ими становится значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
"""

from itertools import zip_longest
def grouper(iterable, n):
    iter1 = iter(iterable)
    return zip_longest(*[iter1 for _ in range(n)])

