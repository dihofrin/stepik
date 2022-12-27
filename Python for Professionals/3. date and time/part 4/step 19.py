"""
https://stepik.org/lesson/570050/step/19?unit=564593

Продуктивность
Артуру нужно подготовить 1010 задач для нового курса "ООП на Python". Чтобы занятие не оказалось утомительным, он придумал правило:

если сегодня он подготовил первую задачу, то вторую он должен подготовить через один день
если сегодня он подготовил вторую задачу, то третью он должен подготовить через два дня
если сегодня он подготовил третью задачу, то четвертую он должен подготовить через три дня
и так далее
Напишите программу, которая определяет даты, в которые Артуру нужно подготовить задачи.

Формат входных данных
На вход программе подается дата подготовки первой задачи в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести 1010 дат, удовлетворяющих условию задачи, каждую на отдельной строке, в формате DD.MM.YYYY.

Примечание. Тестовые данные доступны по ссылке.

Sample Input 1:

20.12.2021
Sample Output 1:

20.12.2021
22.12.2021
25.12.2021
29.12.2021
03.01.2022
09.01.2022
16.01.2022
24.01.2022
02.02.2022
12.02.2022
Sample Input 2:

05.11.2021
Sample Output 2:

05.11.2021
07.11.2021
10.11.2021
14.11.2021
19.11.2021
25.11.2021
02.12.2021
10.12.2021
19.12.2021
29.12.2021
"""

from datetime import datetime, timedelta
d = datetime.strptime(input(), '%d.%m.%Y')
delta = 2
print(d.strftime('%d.%m.%Y'))
for i in range(9):
    d = d + timedelta(days=delta)
    print(d.strftime('%d.%m.%Y'))
    delta += 1
