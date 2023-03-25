"""
https://stepik.org/lesson/570050/step/15?unit=564593

Предыдущая и следующая даты
Напишите программу, которая принимает на вход дату и выводит предыдущую и следующую даты.

Формат входных данных
На вход программе подается дата в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести предыдущую и следующую даты относительно введенной даты, каждую на отдельной строке, в формате DD.MM.YYYY.

Примечание 1. Гарантируется, что у подаваемой даты есть предыдущая и следующая даты.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

04.11.2021
Sample Output 1:

03.11.2021
05.11.2021
Sample Input 2:

30.11.2021
Sample Output 2:

29.11.2021
01.12.2021
Sample Input 3:

01.11.2021
Sample Output 3:

31.10. Iterators & generators.2021
02.11.2021
"""

from datetime import date, datetime,timedelta
dt = datetime.strptime(input(), '%d.%m.%Y')
previous = date(dt.year, dt.month, dt.day) + timedelta(days=-1)
next = date(dt.year, dt.month, dt.day) + timedelta(days=1)
for i in (previous, next):
    print(i.strftime('%d.%m.%Y'))