"""
https://stepik.org/lesson/640048/step/26?unit=636568

Функция palindromes()
Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных чисел-палиндромов.

Примечание 1. Число-палиндром — число, которое читается одинаково как справа налево, так и слева направо.
"""

def palindromes():
    start = 1
    while True:
        if str(start) == str(start)[::-1]:
            yield start
        start += 1
