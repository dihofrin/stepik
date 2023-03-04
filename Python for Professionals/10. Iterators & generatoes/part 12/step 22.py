"""
https://stepik.org/lesson/680669/step/22?unit=679339

Системы счисления
Напишите программу, которая генерирует в системе счисления n все числа длины m.

Формат входных данных
На вход программе в первой строке подается натуральное число n ≤ 16 — основание системы счисления,
а затем натуральное число m — длина генерируемых чисел.

Формат выходных данных
Программа должна сгенерировать в системе счисления n все числа длины m и вывести их в порядке возрастания через пробел.
"""

from itertools import product

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
n, m = int(input()), int(input())
nums = product(nums[:n], repeat=m)

for i in nums:
    print(''.join(i), end=' ')
