"""
https://stepik.org/lesson/674986/step/12?unit=673426

Группы слов
Напишите программу, которая группирует слова по их длине.

Формат входных данных
На вход программе подается последовательность слов, разделенных пробелом. Каждое слово записано строчными латинскими буквами.

Формат выходных данных
Программа должна сгруппировать введенные слова по их длине и вывести полученные группы. Для каждой группы должна быть указана длина, а затем через запятую перечислены слова, имеющие соответствующую длину. Группы должны быть расположены в порядке увеличения длины, каждая на отдельной строке, слова в группах — в алфавитном порядке, в следующем формате:
"""

from itertools import groupby

for k, v in groupby(sorted(input().split(), key=len), key=len):
    print(f'{k} -> {", ".join(sorted(v))}')

