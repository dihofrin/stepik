"""
https://stepik.org/lesson/640048/step/16?unit=636568

Функция alternating_sequence()
Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:

count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный знакочередующийся ряд натуральных чисел.

Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий исключение StopIteration.
"""

def alternating_sequence(count=None):
    start = 1
    if count:
        while True:
            if start <= count:
                if not start % 2:
                    yield start * -1
                else:
                    yield start
            else:
                return StopIteration
            start += 1
    else:
        while True:
            if not start % 2:
                yield start * -1
            else:
                yield start
            start += 1