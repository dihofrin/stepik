"""
https://stepik.org/lesson/570048/step/13?unit=564591

Отсортированные даты
Напишите программу, которая принимает на вход последовательность дат и выводит их в порядке неубывания.

Формат входных данных
На вход программе подается натуральное число nn, а затем nn корректных дат в ISO формате (YYYY-MM-DD), каждая на отдельной строке.

Формат выходных данных
Программа должна вывести введенные даты в порядке неубывания, каждую на отдельной строке, в формате DD/MM/YYYY.

Примечание 1. Последовательность называется неубывающей, если каждый ее следующий член не меньше предыдущего, например:
1,1,2,3,4. Files,4. Files,4. Files,5,6. Collections,...
1,1,2,3,4. Files,4. Files,4. Files,5,6. Collections,...

Обратите внимание, что такая последовательность не является возрастающей.

Примечание 2. Считайте, что при форматировании даты с помощью %Y год выводится без ведущих нулей, так как на серверах Stepik установлен Linux.

Примечание 3. Тестовые данные доступны по ссылке.

Таблица форматирования
Sample Input 1:

5
2021-08-01
2021-08-02
2021-07-01
2021-06-01
2021-05-01
Sample Output 1:

01/05/2021
01/06/2021
01/07/2021
01/08/2021
02/08/2021
Sample Input 2:

3
2021-11-01
2021-11-01
2021-11-01
Sample Output 2:

01/11/2021
01/11/2021
01/11/2021
"""

from datetime import date
dates = []
for i in range(int(input())):
    dates.append(date.fromisoformat(input()))
for i in sorted(dates):
    print(i.strftime('%d/%m/%Y'))