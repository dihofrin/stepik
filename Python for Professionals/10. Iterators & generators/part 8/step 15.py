"""
https://stepik.org/lesson/640045/step/15?unit=636565

Реализуйте функцию tabulate(), которая принимает один аргумент:

func — произвольная функция
Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность возвращаемых значений функции func сначала с аргументом
1, затем 2, затем 3, и так далее."""

from itertools import count

def tabulate(func):
    s = count(1)
    for i in s:
        yield func(i)
