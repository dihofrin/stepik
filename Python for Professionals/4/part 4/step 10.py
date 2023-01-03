"""
https://stepik.org/lesson/623073/step/10?unit=618703

Я исповедую Python, а ты?
Вам доступен файл countries.json, содержащий список JSON-объектов c информацией о странах и исповедуемых в них религиях:

[
   {
      "country": "Afghanistan",
      "religion": "Islam"
   },
   {
      "country": "Albania",
      "religion": "Islam"
   },
   ...
]
Каждый объект из этого списка содержит два атрибута:

country — страна
religion — исповедуемая религия
Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии, а в качестве значения — список стран, в которых исповедуется данная религия. Полученный JSON-объект программа должна записать в файл religion.json.

Примечание 1. Страны в списках должны располагаться в своем исходном порядке.

Примечание 2. Начальная часть файла religion.json выглядит так:

{
   "Islam":[
      "Afghanistan",
      "Albania",
      "Algeria",
      ...
   ],
   ...
}
Примечание 3. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/623073/countries.json
"""

import json
import os

#import wget
#wget.download('https://stepik.org/media/attachments/lesson/623073/countries.json')

with open('countries.json', encoding='utf-8') as file, open('religion.json', 'w', encoding='utf-8') as output:
    data = json.load(file)
    out = dict()
    for i in data:
        out[i['religion']] = out.get(i['religion'], []) + [i['country']]
    json.dump(out, output)
os.remove('countries.json')
#os.remove('religion.json')