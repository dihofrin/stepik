"""
https://stepik.org/lesson/570049/step/12?unit=564592

Функция get_days_in_month()
Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:

year — натуральное число
month — полное название месяца на английском
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month и года year.

Примечание 1. Например, вызов:

get_days_in_month(2021, 'December')
должен вернуть список:

[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., datetime.date(2021, 12, 30), datetime.date(2021, 12, 31)]
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_days_in_month(), но не код, вызывающий ее.
"""

import calendar
from datetime import date

def get_days_in_month(year: int, month: str) -> list:
    result = []
    m = list(calendar.month_name).index(month)
    days = calendar.monthrange(year, m)[1]
    for i in range(1, days+1):
        result.append(date(year, m, i))
    return result