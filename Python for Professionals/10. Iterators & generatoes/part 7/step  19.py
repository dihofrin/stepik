"""
https://stepik.org/lesson/673155/step/19?unit=671418

Функция unique()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность элементов итерируемого объекта iterable без дубликатов.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
"""

def unique(iterable):
    s = list()
    for i in iterable:
        if i not in s:
            s += [i]
            yield i

