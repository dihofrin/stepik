"""
https://stepik.org/lesson/674263/step/16?unit=672698

Функция ncycles()
Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
times — натуральное число
Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, зацикленных times раз.
"""

from itertools import chain, tee

def ncycles(iterable, times):
    for i in tee(iterable, times):
        yield from chain(i)

print(*ncycles([1, 2, 3, 4], 3))