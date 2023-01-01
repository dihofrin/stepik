"""
https://stepik.org/lesson/570049/step/11?unit=564592

Количество дней 😎
Напишите программу, которая определяет количество дней в заданном месяце.

Формат входных данных
На вход программе подаются год и полное название месяца на английском, разделенные пробелом.

Формат выходных данных
Программа должна вывести единственное число — количество дней в введенном месяце.

Sample Input 1:

1983 January
Sample Output 1:

31
Sample Input 2:

1956 February
Sample Output 2:

29
Sample Input 3:

1959 March
Sample Output 3:

31
"""

import calendar

year, month = input().split()

print(calendar.monthrange(int(year), list(calendar.month_name).index(month))[1])