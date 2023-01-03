"""
https://stepik.org/lesson/547172/step/16?unit=540798

Наилучший показатель
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит название файла из этого архива, который имеет наилучший показатель степени сжатия.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Гарантируется, что в исходном архиве только один файл имеет наилучший показатель степени сжатия.


Примечание 4. Указанный архив доступен по ссылке https://stepik.org/media/attachments/lesson/547172/workbook.zip
"""

from zipfile import ZipFile
import os

with ZipFile('workbook.zip') as file:
    info = file.infolist()
    files = {}
    k = lambda x:  x.compress_size / x.file_size
    for i in info:
        try:
            filename = i.filename.split('/')
            if len(filename) == 1:
                files[filename[0]] = k(i)
            else:
                files[filename[1]] = k(i)
        except ZeroDivisionError:
            pass
    print(min(files, key=files.get))