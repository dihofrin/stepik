"""
https://stepik.org/lesson/547172/step/14?unit=540798

Количество файлов
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит единственное число — количество файлов в этом архиве.

Примечание 1. Обратите внимание, что папка не считается файлом.

Примечание 2. Указанный архив доступен по ссылке https://stepik.org/media/attachments/lesson/547172/workbook.zip
"""

from zipfile import ZipFile
import os

#import wget
#wget.download('https://stepik.org/media/attachments/lesson/547172/workbook.zip')

with ZipFile('workbook.zip') as file:
    info = file.infolist()
    print(len([i for i in info if not i.is_dir()]))
#os.remove('workbook.zip')