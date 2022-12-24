"""
https://stepik.org/lesson/570048/step/16?unit=564591

Корректные даты
Напишите программу, которая принимает на вход последовательность дат и проверяет каждую из них на корректность.

Формат входных данных
На вход программе подается последовательность дат в формате DD.MM.YYYY, каждая на отдельной строке. Концом последовательности является слово end.

Формат выходных данных
Программа должна для каждой введенной даты вывести текст Корректная или Некорректная в зависимости от того, является ли дата корректной, а затем вывести количество корректных дат.

Примечание 1. Для анализа даты на корректность можете использовать уже реализованную функцию is_correct() из предыдущей задачи.

Примечание 2. Тестовые данные доступны по ссылке.

Таблица форматирования
Sample Input 1:

19.05.2016
05.13.2010
21.12.2012
01.01.1000
32.04.2003
end
Sample Output 1:

Корректная
Некорректная
Корректная
Корректная
Некорректная
3
Sample Input 2:

15.02.1524
29.02.2017
27.05.1528
13.10.1736
40.06.431
31.07.5200
29.02.2016
end
Sample Output 2:

Корректная
Некорректная
Корректная
Корректная
Некорректная
Корректная
Корректная
5
"""

from datetime import date
c = 0
def is_correct(inp):
    try:
       day, month, year = inp.split('.')
       dt = date(int(year), int(month), int(day))
       global c
       c += 1
       print('Корректная')
    except ValueError:
       print('Некорректная')
while True:
    dt = input()
    if dt == 'end':
        break
    is_correct(dt)
print(c)