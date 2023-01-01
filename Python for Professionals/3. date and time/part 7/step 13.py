"""
https://stepik.org/lesson/570049/step/13?unit=564592

Функция get_all_mondays()
Реализуйте функцию get_all_mondays(), которая принимает один аргумент:

year — натуральное число
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на понедельник.

Примечание 1. Например, вызов:

get_all_mondays(2021)
должен вернуть список:

[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_mondays(), но не код, вызывающий ее.
"""

from datetime import date

def get_all_mondays(year: int) -> list:
    d = date(year, 1, 1).toordinal()
    nd = date(year+1, 1, 1).toordinal()
    return [date.fromordinal(i) for i in range(d, nd) if date.fromordinal(i).weekday() == 0]