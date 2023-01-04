"""
https://stepik.org/lesson/623073/step/7?unit=618703

Разные типы
Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]
Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическое значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется
Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
то программа должна была бы создать файл updated_data.json со следующим содержанием:

["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]
Примечание 2. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/623073/data.json
"""

import json
#import wget
import os

#wget.download('https://stepik.org/media/attachments/lesson/623073/data.json')

with open('data.json') as file:
    d = json.load(file)
    result = []
    with open('updated_data.json', 'w', encoding='utf-8') as u:
        for i in d:
            if type(i) is str:
                result.append(i+'!')
            if type(i) is bool:
                result.append(not i)
            if type(i) is int:
                result.append(i+1)
            if type(i) is list:
                result.append([*i, *i])
            if type(i) is dict:
                i.update({'newkey': None})
                result.append(i)
        json.dump(result, u)
os.remove('data.json')