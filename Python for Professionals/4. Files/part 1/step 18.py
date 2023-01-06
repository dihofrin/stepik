"""
https://stepik.org/lesson/520159/step/18?unit=512678

Гуру прогрессий
Дана последовательность целых чисел. Напишите программу, которая определяет, является ли данная последовательность прогрессией, и если да, то определяет её вид.

Формат входных данных
На вход программе подается произвольное количество строк (не менее трёх), в каждой строке записано натуральное число — очередной член последовательности.

Формат выходных данных
Программа должна вывести текст:

Арифметическая прогрессия, если введенная последовательность чисел является арифметической прогрессией
Геометрическая прогрессия, если введенная последовательность чисел является геометрической прогрессией
Не прогрессия, если введенная последовательность чисел не является прогрессией
"""

import sys

data = [int(i) for i in sys.stdin]
n = len(data)
if data[n-1] / data[n-2] == data[n-2] / data[n-3] and data[2] / data[1] == data[1] / data[0] and data[2] > data[1] and data[n-1] > data[n-2]:
    print('Геометрическая прогрессия')
elif data[n-1] - data[n-2] == data[n-2] - data[n-3] and data[2] - data[1] == data[1] - data[0]:
    print('Арифметическая прогрессия')
else:
    print('Не прогрессия')