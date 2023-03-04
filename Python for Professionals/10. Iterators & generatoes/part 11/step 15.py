"""
https://stepik.org/lesson/674986/step/15?unit=673426


"""

from itertools import groupby

def ranges(numbers):
    g = groupby(numbers, key=lambda x: x-numbers.index(x))
    result = []
    for k, v in g:
        tmp = list(v)
        result.append((tmp[0], tmp[-1]))
    return result
