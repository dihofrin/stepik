"""
https://stepik.org/lesson/570049/step/9?unit=564592

День недели
Напишите программу, которая определяет день недели, соответствующий заданной дате.

Формат входных данных
На вход программе подается дата в формате YYYY-MM-DD.

Формат выходных данных
Программа должна вывести полное название дня недели на английском, который соответствует введенной дате.

Sample Input 1:

2021-12-10. Iterators & generators
Sample Output 1:

Friday
Sample Input 2:

2022-01-03
Sample Output 2:

Monday
Sample Input 3:

2021-11-02
Sample Output 3:

Tuesday
"""

import calendar

year, month, day = map(int, input().split('-'))

print(list(calendar.day_name)[calendar.weekday(year, month, day)])