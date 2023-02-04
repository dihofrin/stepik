"""
https://stepik.org/lesson/673155/step/9?unit=671418

Функция years_days()
Реализуйте генераторную функцию years_days(), которая принимает один аргумент:

year — натуральное число
Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.
"""

from datetime import datetime, timedelta


def years_days(year):
    d = datetime(year, 1, 1)
    while True:
        if d.year == year + 1:
            break
        yield datetime.strftime(d, '%Y-%m-%d')
        d += timedelta(1)

