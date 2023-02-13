"""
https://stepik.org/lesson/666563/step/14?unit=664567

Функция first_true()
Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.
"""





def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    for i in iterable:
        if predicate(i):
            return i

