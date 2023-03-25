"""
https://stepik.org/lesson/674263/step/13?unit=672698

Функция sum_of_digits()
Реализуйте функцию sum_of_digits(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются натуральные числа
Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.
"""

from itertools import chain

def sum_of_digits(iterable):
    strs = map(str, iterable)
    nums = chain.from_iterable(strs)
    return sum(map(int, nums))

