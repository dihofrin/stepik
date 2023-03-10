"""
https://stepik.org/lesson/570049/step/7?unit=564592

Високосный год
Напишите программу, которая определяет, является ли год високосным.

Формат входных данных
На вход программе в первой строке подается целое число nn, в последующих nn строках вводятся натуральные числа, представляющие года.

Формат выходных данных
Программа должна для каждого введенного года вывести True, если он является високосным, или False в противном случае.

Sample Input 1:

1
2021
Sample Output 1:

False
Sample Input 2:

4. Files
1999
2000
2001
2002
Sample Output 2:

False
True
False
False
Sample Input 3:

3
4433
2048
9757
Sample Output 3:

False
True
False
"""

import calendar

for i in range(int(input())):
    print(calendar.isleap(int(input())))