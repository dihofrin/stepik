"""
https://stepik.org/lesson/590120/step/19?unit=585064

The Zen of Python
Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте. Буквы и их количество должны выводиться в лексикографическом порядке, каждая на отдельной строке, в следующем формате:

<буква>: <количество>
Примечание 1. Начальная часть ответа выглядит так:

a: 53
b: 21
...
Примечание 2. Программа не должна учитывать регистр, то есть, например, буквы a и A считаются одинаковыми.

Примечание 3. Программа должна игнорировать все небуквенные символы.

Примечание 4. Files. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/590120/pythonzen.txt
"""

from collections import Counter

#from wget import download

#download('https://stepik.org/media/attachments/lesson/590120/pythonzen.txt')

with open('pythonzen.txt', 'r', encoding='utf-8') as f:
    r = f.read()
    s = Counter(i.lower() for i in r if i.isalpha())
    for key, value in sorted(s.items()):
        print(f'{key}: {value}')