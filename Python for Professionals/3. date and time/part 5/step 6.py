"""
https://stepik.org/lesson/571244/step/6?unit=565785

Сотрудники организации 🙂
Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения. Напишите программу, которая определяет, в какую из дат родилось больше всего сотрудников.

Формат входных данных
На вход программе в первой строке подается натуральное число nn — количество сотрудников, работающих в организации. В последующих nn строках вводятся данные о каждом сотруднике: имя, фамилия и дата рождения, разделённые пробелом. Дата рождения указывается в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести дату, в которую наибольшее количество сотрудников отмечает день рождения, в формате DD.MM.YYYY. Если таких дат несколько, программа должна вывести их все в порядке возрастания, каждую на отдельной строке, в том же формате.

Примечание. Тестовые данные доступны по ссылке.

Sample Input 1:

5
Иван Петров 01.05.1995
Петр Сергеев 29.04.1995
Сергей Романов 01.01.1996
Роман Григорьев 01.01.1996
Григорий Иванов 01.05.1995
Sample Output 1:

01.05.1995
01.01.1996
Sample Input 2:

5
Иван Петров 14.10.1995
Петр Сергеев 29.04.1992
Сергей Романов 01.01.1994
Роман Григорьев 01.01.1994
Григорий Иванов 16.07.1995
Sample Output 2:

01.01.1994
"""

from datetime import date, timedelta, datetime

pattern = '%d.%m.%Y'
n = int(input())
dates1 = {}
for i in range(n):
    name, surname, date = input().split()
    z = datetime.strptime(date, pattern)
    dates1[z] = dates1.get(z, 0) + 1
x = max(dates1.values())
dates = sorted([i for i in dates1.keys() if dates1[i] == x])
for i in dates:
    print(datetime.strftime(i, pattern))