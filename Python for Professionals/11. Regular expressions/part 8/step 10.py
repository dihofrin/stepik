"""
https://stepik.org/lesson/680266/step/10?unit=678924

Функция normalize_whitespace()
Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:

string — произвольная строка
Функция должна заменять все множественные пробелы в строке string на единственный пробел и возвращать полученный результат.
"""

import re

def normalize_whitespace(string):
    return re.sub(r'\s+', r' ', string)