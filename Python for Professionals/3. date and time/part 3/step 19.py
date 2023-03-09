"""
https://stepik.org/lesson/611754/step/19?unit=607091

time
17 из 19 шагов пройдено
36 из 56 баллов  получено
Функция is_available_date() 🌶️
Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для бронирования. В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.

"""

import datetime

def ordinal(date):
    dt = list(map(int, date.split('.')))
    dt = datetime.date(dt[2], dt[1], dt[0]).toordinal()
    return dt

def set_dates(dates):
    booked = []
    for i in dates:
        if '-' in i:
            tmp = i.split('-')
            for j in range(ordinal(tmp[0]), ordinal(tmp[1]) + 1):
                booked.append(j)
        else:
            booked.append(ordinal(i))
    return set(booked)

def is_available_date(booked_dates, date_for_booking):
    booked = set_dates(booked_dates)
    if '-' in date_for_booking:
        dates = set_dates([date_for_booking])
        return not bool(dates & booked)
    else:
        return ordinal(date_for_booking) not in booked

