"""
https://stepik.org/lesson/571244/step/5?unit=565785

Сотрудники организации 😄
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая определяет самого старшего сотрудника из данного списка.

Формат входных данных
На вход программе в первой строке подается натуральное число nn — количество сотрудников, работающих в организации. В последующих nn строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна определить самого старшего сотрудника и вывести его дату рождения, имя и фамилию, разделив пробелом. Если таких сотрудников несколько, программа должна вывести их дату рождения, а также их количество, разделив пробелом.

Примечание 1. Гарантируется, что у всех сотрудников имена и фамилии различны.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

3
Иван Петров 01.05.1995
Петр Сергеев 29.04.1995
Сергей Иванов 01.01.1996
Sample Output 1:

29.04.1995 Петр Сергеев
Sample Input 2:

3
Иван Петров 01.05.1995
Петр Сергеев 29.05.1995
Сергей Иванов 01.05.1995
Sample Output 2:

01.05.1995 2
"""

from datetime import date, timedelta, datetime

pattern = '%d.%m.%Y'
n = int(input())
dates1, dates2 = {}, {}
for i in range(n):
    name, surname, date = input().split()
    z = datetime.strptime(date, pattern)
    if z not in dates1:
        dates1[z] = [(name, surname)]
    else:
        dates1[z].append((name, surname))
    dates2[z] = dates2.get(z, 0) + 1
if len(dates2) < n:
     print(max(dates2, key=dates2.get).strftime(pattern), dates2[max(dates2, key=dates2.get)])
else:
    x = min(dates1.keys())
    print(datetime.strftime(x, pattern), ' '.join(*dates1[x]))