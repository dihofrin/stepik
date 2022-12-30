"""
https://stepik.org/lesson/570050/step/17?unit=564593

Таймер
Часы показывают время в формате HH:MM:SS. На этих часах запустили таймер, который прозвенит через nn секунд. Напишите программу, которое определит, какое время будет на часах, когда прозвенит таймер.

Формат входных данных
На вход программе в первой строке подается текущее время на часах в формате HH:MM:SS. В следующей строке вводится целое неотрицательное число nn — количество секунд, через которое должен прозвенеть таймер.

Формат выходных данных
Программа должна вывести время в формате HH:MM:SS, которое будет на часах, когда прозвенит таймер.

Примечание. Тестовые данные доступны по ссылке.

Sample Input 1:

09:00:00
90
Sample Output 1:

09:01:30
Sample Input 2:

23:59:59
1
Sample Output 2:

00:00:00
Sample Input 3:

13:34:46
456
Sample Output 3:

13:42:22
"""

from datetime import date, datetime,timedelta
dt = datetime.strptime(input(), '%H:%M:%S')
timer = int(input())
print((dt + timedelta(seconds=timer)).strftime('%H:%M:%S'))