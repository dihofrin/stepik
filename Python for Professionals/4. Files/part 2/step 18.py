"""
https://stepik.org/lesson/518491/step/18?unit=510939

Лог-файл
Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. В первом столбце записано измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. При этом email пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...
Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя и записывает их в файл new_name_log.csv. В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие же, как в файле name_log.csv. Логи в итоговом файле должны быть расположены в лексикографическом порядке названий электронных ящиков пользователей.

Примечание 1. Для части пользователей в исходном файле запись только одна, и тогда в итоговый файл следует записать только ее, для некоторых пользователей есть несколько записей с разными именами.

Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:

C=3PO,c3po@gmail.com,16/11/2021 17:10
C3PO,c3po@gmail.com,16/11/2021 17:15
C-3PO,c3po@gmail.com,16/11/2021 17:24
Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:

C-3PO,c3po@gmail.com,16/11/2021 17:24
Примечание 2. Разделителем в файле name_log.csv является запятая, при этом кавычки не используются.

Примечание 3. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/518491/name_log.csv

Примечание 4. Files. Начальная часть файла new_name_log.csv выглядит так:

username,email,dtime
angry-barbara2,barbaraanderson@bk.ru,17/11/2021 01:17
dead-barbara6,barbarabrown@rambler.ru,27/11/2021 08:27
busy_barbara7,barbaradavis@aol.com,24/11/2021 08:24
...
Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
"""

import csv, os
from datetime import datetime

#import wget
#wget.download('https://stepik.org/media/attachments/lesson/518491/name_log.csv')

pattern = '%d/%m/%Y %H:%M'


with open('name_log.csv', 'r', encoding='utf-8') as file:
    data = list(csv.reader(file))[1:]
    result = dict()
    for i in data:
        if i[1] not in result:
            result[i[1]] = [i[2], i[0]]
        else:
            if datetime.strptime(i[2], pattern) > datetime.strptime(result[i[1]][0], pattern):
                result[i[1]] = [i[2], i[0]]
with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as output_file:
    columns = ['username', 'email', 'dtime']
    writer = csv.writer(output_file)
    writer.writerow(columns)
    for key, value in sorted(result.items()):
        row = [value[1], key, value[0]]
        writer.writerow(row)
os.remove('name_log.csv')