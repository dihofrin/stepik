"""
https://stepik.org/lesson/547172/step/17?unit=540798

Избранные
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Начальная часть ответа выглядит так:

countries.json
data_sample.csv
...
Примечание 3. Указанный архив доступен по ссылке https://stepik.org/media/attachments/lesson/547172/workbook.zip
"""

from zipfile import ZipFile
from datetime import datetime

t = datetime(2021, 11, 30, 14, 22)
dates = []
with ZipFile('workbook.zip') as file:
    info = file.infolist()
    for i in info:
        if not i.is_dir():
            if datetime(i.date_time[0], i.date_time[1], i.date_time[2], i.date_time[3], i.date_time[4]) > t:
                dates.append(i.filename.split('/')[-1])
    print(*sorted(dates), sep='\n')