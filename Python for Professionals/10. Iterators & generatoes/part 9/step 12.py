"""
https://stepik.org/lesson/666563/step/12?unit=664567

Функция drop_while_negative()
Реализуйте функцию drop_while_negative(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются целые числа
Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable, начиная с первого неотрицательного числа.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться в своем исходном порядке.
"""

from itertools import dropwhile
def drop_while_negative(iterable):
    yield from dropwhile(lambda x: x < 0, iterable)

