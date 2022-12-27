"""
https://stepik.org/lesson/570050/step/18?unit=564593

Функция num_of_sundays()
Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:

year — натуральное число, год
Функция должна возвращать количество воскресений в году year.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию num_of_sundays(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

print(num_of_sundays(2021))
Sample Output 1:

52
Sample Input 2:

year = 2000
print(num_of_sundays(year))
Sample Output 2:

53
Sample Input 3:

print(num_of_sundays(768))
Sample Output 3:

52
"""

from datetime import datetime, timedelta
def num_of_sundays(year):
    x = year
    now = datetime(year=x, month=1, day=1)
    c = 0
    while now.year != x + 1:
        if now.strftime('%A') == 'Sunday':
            c += 1
        now += timedelta(days=1)
    return c