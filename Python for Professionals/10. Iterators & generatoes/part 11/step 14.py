"""
https://stepik.org/lesson/674986/step/14?unit=673426

Функция group_anagrams()
Анаграммы — это слова, которые состоят из одинаковых букв. Например:

адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка
Реализуйте функцию group_anagrams(), которая принимает один аргумент:

words — список слов
Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, и возвращать список полученных кортежей.
"""

from itertools import groupby

def group_anagrams(words):
    g = groupby(sorted(words, key=sorted), key=sorted)
    for k, v in g:
        yield tuple(v)

