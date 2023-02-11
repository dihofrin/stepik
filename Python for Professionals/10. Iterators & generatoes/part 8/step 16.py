"""
https://stepik.org/lesson/640045/step/16?unit=636565

Функция factorials()
Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:

n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых является факториалом очередного натурального числа.

"""

from itertools import accumulate
from operator import mul
def factorials(n):
    return accumulate(range(1, n+1), func=mul)

numbers = factorials(6)

print(*numbers)