"""
https://stepik.org/lesson/520159/step/11?unit=512678

Размах данных
Дана последовательность дат. Напишите программу, которая выводит количество дней между максимальной и минимальной датами данной последовательности.

Формат входных данных
На вход программе подается произвольное количество строк, в каждой строке записана дата в ISO формате (YYYY-MM-DD).

Формат выходных данных
Программа должна вывести единственное число — количество дней между максимальной и минимальной датами введенной последовательности.
"""
import sys, datetime

data = [datetime.datetime.fromisoformat(line.strip()) for line in sys.stdin]
sys.stdout.write(str((max(data)-min(data)).days))