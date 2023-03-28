"""
https://stepik.org/lesson/666563/step/13?unit=664567

Функция drop_this()
Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
obj — произвольный объект
Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, начиная с элемента, не равного obj.
"""

from itertools import dropwhile
def drop_this(iterable, obj):
    yield from dropwhile(lambda x: x == obj, iterable)

