"""
https://stepik.org/lesson/668595/step/16?unit=666704

Функция random_numbers()
Реализуйте функцию random_numbers(), которая принимает два аргумента:

left — целое число
right — целое число
Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых чисел в диапазоне от left до right включительно.

Примечание 1. Гарантируется, что left <= right.
"""

from random import randint
def random_numbers(left, right):
    return iter(lambda: randint(left, right), '0')

