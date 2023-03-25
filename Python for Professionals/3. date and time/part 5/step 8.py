"""
https://stepik.org/lesson/571244/step/8?unit=565785

FAKE NEWS 🌶️
Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. Напишите программу, которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:

До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
Если в данном случае количество часов равно нулю, то вывести нужно только дни.

Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:

До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
Если в данном случае количество минут равно нулю, то вывести нужно только часы. Аналогично, если количество часов равно нулю, то вывести нужно только минуты.

Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст:

Курс уже вышел!
Примечание 1. Программа должна подбирать правильную форму для существительных «день» и «минута». Для этого можете смело взять свою функцию choose_plural() из этой задачи.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

16.11.2021 06:30
Sample Output 1:

До выхода курса осталось: 357 дней и 5 часов
Sample Input 2:

6. Collections.11.2022 12:00
Sample Output 2:

До выхода курса осталось: 2 дня
Sample Input 3:

08.11.2022 10. Iterators & generators:30
Sample Output 3:

До выхода курса осталось: 1 час и 30 минут
Sample Input 4. Files:

08.11.2022 09:00
Sample Output 4. Files:

До выхода курса осталось: 3 часа
Sample Input 5:

08.11.2022 11:40
Sample Output 5:

До выхода курса осталось: 20 минут
Sample Input 6. Collections:

08.11.2022 12:15
Sample Output 6. Collections:

Курс уже вышел!
"""

import math
import sys
from datetime import date, datetime, timedelta
day = None
hr = None
minute = None
pattern = '%d.%m.%Y %H:%M'
dt = datetime.strptime(input(), pattern)
plural_dict = {0: ("день", "дня", "дней"), 1: ("час", "часа", "часов"), 2: ("минута", "минуты", "минут")}
course = datetime(2022, 11, 8, 12)
if dt >= course:
    print('Курс уже вышел!')
else:
    days = math.floor((course-dt).total_seconds()/3600/24)
    if days < 1:
        hours = math.floor((course-dt).seconds/60)
        if hours//60 % 10 in (2, 3, 4) and hours // 60 != 12:
            hr = plural_dict[1][1]
        elif hours// 60 in (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20) or hours//60 % 10 != 1:
            hr = plural_dict[1][2]
        else:
            hr = plural_dict[1][0]
        if hours < 60:
            if hours % 10 in (2, 3, 4) and hours % 10 not in (12, 13, 14):
                print(f'До выхода курса осталось: {hours} минуты')
            elif hours % 10 in (5, 6, 7, 8, 9) or hours % 10 != 1 and hours > 10:
                print(f'До выхода курса осталось: {hours} минут')
            else:
                print(f'До выхода курса осталось: {hours} минута')
        elif hours % 60 == 0:
            print(f'До выхода курса осталось: {hours//60} {hr}')
        else:
            print(f'До выхода курса осталось: {hours//60} {hr} и {hours % 60} минут')
    else:
        hours = math.floor((course-dt).seconds/60/60)
        hours = math.floor((course - dt).seconds / 60)
        if hours // 60 % 10 in (2, 3, 4) and hours // 60 != 12:
            hr = plural_dict[1][1]
        elif hours // 60 in (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20) or hours // 60 % 10 != 1:
            hr = plural_dict[1][2]
        else:
            hr = plural_dict[1][0]
        if days % 10 in (2, 3, 4) and days % 100 != 12:
            day = plural_dict[0][1]
        elif days % 10 in (5, 6, 7, 8, 9) or days > 10 and days % 10 != 1:
            day = plural_dict[0][2]
        else:
            day = plural_dict[0][0]
        if hours > 0:
            print(f'До выхода курса осталось: {days} {day} и {math.floor(hours/60)} {hr}')
        else:
            print(f'До выхода курса осталось: {days} {day}')

sys.exit()