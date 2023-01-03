"""
https://stepik.org/lesson/623073/step/8?unit=618703

Вам доступны два файла data1.json и data2.json, каждый из которых содержит по единственному JSON-объекту:

{
   "Holly-Anne": [
      33,
      "failed"
   ],
   "Caty": [
      36,
      "failed"
   ],
   ...
}
Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, причем если пары из первого и второго объектов имеют совпадающие ключи, то значение следует взять из второго объекта. Полученный JSON-объект программа должна записать в файл data_merge.json.

Примечание 1. Например, если бы файлы data1.json и data2.json имели вид:

{
   "Timur": 99,
   "Anri": 97
}
{
   "Dima": 99,
   "Anri": 100
}
то программа должна была бы создать файл data_merge.json со следующим содержанием:

{
   "Anri": 100,
   "Dima": 99,
   "Timur": 99
}
Примечание 2. Элементы в результирующем JSON-объекте могут располагаться в произвольном порядке.

Примечание 3. Указанные файлы доступны по ссылке https://stepik.org/media/attachments/lesson/623073/data1.json
 и ссылке https://stepik.org/media/attachments/lesson/623073/data2.json.
"""

import json
import os
#import wget

#wget.download('https://stepik.org/media/attachments/lesson/623073/data1.json')
#wget.download('https://stepik.org/media/attachments/lesson/623073/data2.json')

with open('data1.json', encoding='utf-8') as d1, open('data2.json', encoding='utf-8') as d2, open('data_merge.json', 'w', encoding='utf-8') as d3:
    data1 = json.load(d1)
    data2 = json.load(d2)
    json.dump({**data1, **data2}, d3)
os.remove('data1.json')
os.remove('data2.json')