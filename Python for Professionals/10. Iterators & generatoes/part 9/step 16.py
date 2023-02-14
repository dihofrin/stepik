"""
https://stepik.org/lesson/666563/step/16?unit=664567

Функция take_nth()
Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число
Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable. Если итерируемый объект iterable содержит менее n элементов, функция должна вернуть значение None.
"""

from itertools import islice
def take_nth(iterable, n):
        return next(islice(iterable, n-1, n), None)

