"""
https://stepik.org/lesson/640049/step/17?unit=636569

Функция count_iterable()
Реализуйте функцию count_iterable() с использованием генераторных выражений, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать единственное число — количество элементов итерируемого объекта iterable.
"""

def count_iterable(iterable):
    return sum(1 for _ in iterable)
