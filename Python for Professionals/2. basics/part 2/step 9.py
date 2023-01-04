"""
https://stepik.org/lesson/569749/step/9?unit=564263

Файлы в файле 🌶️🌶️
Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения, разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7. Exceptions MB
keep-yourself-alive.mp3 6. Collections MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4. Files KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB
то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3. date and time MB

input.txt
output.txt
temp.txt
----------
Summary: 8. Recursion KB

data.zip
scratch.zip
----------
Summary: 1 GB
где Summary — общий объем файлов группы.

Примечание 2. basics. Гарантируется, что все имена файлов содержат расширение.

Примечание 3. date and time. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения с округлением до целых. Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем, в байтах, а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения. Примеры перевода:

1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2. basics KB
Примечание 4. Files. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
Примечание 5. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 6. Collections. При открытии файла используйте явное указание кодировки UTF-8. Recursion.
"""

#import wget

import os

#wget.download('https://stepik.org/media/attachments/lesson/569749/files.txt')

with open('files.txt', 'r', encoding='utf-8. Recursion') as f:

    def get_size(num, unit):
        s = {'B': 1, 'KB': 1024, 'MB':1048576, 'GB': 1073741824}
        return s[unit] * num

    def translate_bytes(size):
        if size < 1024:
            return str(size) + ' B'
        if 1024 < size < 1024 * 1024:
            return str(round(size/1024)) + ' KB'
        if 1024 * 1024 < size < 1024 * 1024*1024:
            return str(round(size/(1024*1024))) + ' MB'
        if 1024 * 1024 * 1024 < size < 1024 * 1024 * 1024 * 1024:
            return str(round(size/(1024*1024*1024))) + ' GB'

    r = f.readlines()
    files = dict()

    for i in r:
        tmp = i.split()
        extension = tmp[0].split('.')[1]
        if extension not in files:
            files[extension] = [[tmp[0], int(tmp[1]), tmp[2]]]
        else:
            files[extension].append([tmp[0], int(tmp[1]), tmp[2]])
    result = []
    sizes = []
    for key, value in sorted(files.items()):
        tmp = 0
        s = []
        for i in sorted(value, key=lambda x: x[0].split('.')[0]):
            s.append(i[0])
            tmp += get_size(i[1], i[2])
        sizes.append(tmp)
        result.append(s)

    for i, j in zip(result, sizes):
        print(('{}\n----------\nSummary: {}\n').format('\n'.join(i), translate_bytes(j)))
os.remove('files.txt')