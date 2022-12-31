"""
https://stepik.org/lesson/571244/step/7?unit=565785

Сотрудники организации 😔
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая определяет самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней от текущей даты.

Формат входных данных
На вход программе в первой строке подается текущая дата в формате DD.MM.YYYY, в следующей строке вводится натуральное число nn — количество сотрудников, работающих в организации. В последующих nn строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна определить самого молодого сотрудника, празднующего свой день рождения в течение ближайших семи дней, и вывести его имя и фамилию, разделив пробелом. Если таких сотрудников нет, программа должна вывести текст:

Дни рождения не планируются
Примечание 1. Гарантируется, что у всех сотрудников даты рождения различны.

Примечание 2. Например, для даты 01.11.2021 ближайшими семью днями являются:

02.11.2021, 03.11.2021, 04.11.2021, 05.11.2021, 06.11.2021, 07.11.2021, 08.11.2021
Примечание 3. Тестовые данные доступны по ссылке.

Sample Input 1:

14.11.2021
3
Иван Петров 16.11.1995
Петр Сергеев 14.11.1997
Сергей Романов 17.11.1994
Sample Output 1:

Иван Петров
Sample Input 2:

14.11.2021
3
Иван Петров 25.12.1995
Петр Сергеев 24.11.1997
Сергей Романов 28.12.1994
Sample Output 2:

Дни рождения не планируются
"""

from datetime import datetime, timedelta

dates = {}
pattern = '%d.%m.%Y'
dt = datetime.strptime(input(), pattern)
next_days = []
for i in range(7):
    dt += timedelta(days=1)
    next_days.append(dt)

for _ in range(int(input())):
    *names, birthday = input().split()
    birthday = datetime.strptime(birthday, pattern)
    dates[birthday] = names

close = []

for i in dates.keys():
    z = datetime(dt.year, i.month, i.day)
    if z in next_days:
        close.append(i)

if len(close) == 0:
    print('Дни рождения не планируются')
else:
    print(*dates[max(close)])