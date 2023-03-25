"""
https://stepik.org/lesson/570050/step/22?unit=564593


Реп по матеше
Репетитор по математике проводит занятия по 4545 минут с перерывами по 1010 минут. Репетитор обозначает время начала рабочего дня и время окончания рабочего дня. Напишите программу, которая генерирует и выводит расписание занятий.

Формат входных данных
На вход программе в первой строке подается время начала рабочего дня в формате HH:MM. В следующей строке вводится время окончания рабочего дня в том же формате.

Формат выходных данных
Программа должна сгенерировать и вывести расписание занятий. На первой строке выводится время начала и окончания первого занятия в формате HH:MM - HH:MM, на второй строке — время начала и окончания второго занятия в том же формате, и так далее.

Примечание 1. Если занятие обрывается временем окончания работы, то добавлять его в расписание не нужно.

Примечание 2. Если разница между временем начала и окончания рабочего дня меньше 4545 минут, программа ничего не должна выводить.

Примечание 3. Тестовые данные доступны по ссылке.

Sample Input 1:

10. Iterators & generators:00
12:35
Sample Output 1:

10. Iterators & generators:00 - 10. Iterators & generators:45
10. Iterators & generators:55 - 11:40
11:50 - 12:35
Sample Input 2:

09:00
11:00
Sample Output 2:

09:00 - 09:45
09:55 - 10. Iterators & generators:40
Sample Input 3:

11:00
11:30
Sample Output 3:
"""

import sys
from datetime import datetime, timedelta
pattern = '%H:%M'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)
lesson_ending = start + timedelta(minutes=45)
delta = timedelta(minutes=55)
lesson_start = []
lesson_end = []
if end - start < delta:
    sys.exit()
while start < end:
    lesson_start.append(start)
    if start + delta <= end:
        start += delta
    else:
        break
for i in range(len(lesson_start)):
    lesson_end.append(lesson_ending)
    if lesson_ending + delta <= end:
        lesson_ending += delta
    else:
        break
for i in range(len(lesson_end)):
    print(' - '.join((lesson_start[i].strftime(pattern), lesson_end[i].strftime(pattern))))
