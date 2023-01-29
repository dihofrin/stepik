"""
https://stepik.org/lesson/640048/step/18?unit=636568

Реализуйте генераторную функцию reverse(), которая принимает один аргумент:

sequence — последовательность
Функция должна возвращать генератор, порождающий элементы последовательности sequence в обратном порядке, а затем возбуждающий исключение StopIteration.

Примечание 1. Последовательностью является коллекция, поддерживающая индексацию и имеющая длину. Например, объекты типа list, str, tuple являются последовательностями.
"""

def reverse(sequence):
    i = len(sequence) - 1
    while i > -1:
        yield sequence[i]
        i -= 1
