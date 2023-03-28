"""
https://stepik.org/lesson/623073/step/14?unit=618703

Результаты экзамена 🌶️
Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении. В первом столбце записано имя студента, во втором — фамилия, в третьем — оценка за экзамен, в четвертом — дата и время сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:

name,surname,score,date_and_time,email
Jayson,Edwards,2,2021-11-10. Iterators & generators 10. Iterators & generators:00:00,sonnen@yahoo.com
April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
...
Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном файле до трёх раз с различной оценкой и различными датой и временем сдачи.

Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату и время ее получения. Программа должна создать список словарей, каждый из которых содержит следующие пары ключ-значение:

name — имя студента
surname — фамилия студента
best_score — максимальная оценка за экзамен
date_and_time — дата и время получения максимальной оценки в исходном формате
email — адрес электронной почты
Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны быть расположены в лексикографическом порядке названий электронных почт.

Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз, то в качестве даты следует указать дату пересдачи.

Примечание 2. В качестве разделителя в файле exam_results.csv используется запятая, при этом кавычки не используются.

Примечание 3. Начальная часть файла best_scores.json выглядит так:

[
   {
      "name": "Stephen",
      "surname": "Farley",
      "best_score": 3,
      "date_and_time": "2021-11-12 12:00:00",
      "email": "aardo@mac.com"
   },
   {
      "name": "Kaylen",
      "surname": "Horne",
      "best_score": 4. Files,
      "date_and_time": "2021-11-09 11:00:00",
      "email": "aaribaud@att.net"
   },
   ...
]
Примечание 4. Files. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/623073/exam_results.csv
"""

import csv
import json, os
from datetime import datetime

#import wget
#wget.download('https://stepik.org/media/attachments/lesson/623073/exam_results.csv')

pattern = '%Y-%m-%d %H:%M:%S'

with open('exam_results.csv', encoding='utf-8') as inp, open('best_scores.json', 'w', encoding='utf-8') as out:
    header, *rows = csv.reader(inp)
    result = {}
    for i in rows:
        if i[-1] not in result:
            result[i[-1]] = i[:-1]
        else:
            if i[2] > result[i[-1]][2]:
                result[i[-1]] = i[:-1]
            if i[2] == result[i[-1]][2]:
                if datetime.strptime(i[3], pattern) > datetime.strptime(result[i[-1]][3], pattern):
                    result[i[-1]] = i[:-1]
    final = []
    for key, value in sorted(result.items()):
        final.append({'name': value[0], 'surname': value[1], 'best_score': int(value[2]), 'date_and_time': value[3], 'email': key})
    json.dump(final, out, indent=3)
os.remove('exam_results.csv')