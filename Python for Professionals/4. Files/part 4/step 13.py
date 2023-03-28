"""
https://stepik.org/lesson/623073/step/13?unit=618703

Бассейны
Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты в понедельник в период с 10. Iterators & generators:00 до 12:00. Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих в это время бассейнов нужно выбрать бассейн с наибольшей длиной дорожки, при равных значениях — c наибольшей шириной.

Вам доступен файл pools.json, содержащий список JSON-объектов, которые представляют данные о крытых плавательных бассейнах:

[
   {
      "ObjectName": "Физкультурно-оздоровительный комплекс с бассейном «ГБУ «СШОР № 82» Москомспорта»",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Алтуфьевский район",
      "Address": "Инженерная улица, дом 5, корпус 1",
      "WorkingHoursSummer": {
         "Понедельник": "10. Iterators & generators:00-11:00",
         "Вторник": "10. Iterators & generators:00-11:00",
         "Среда": "10. Iterators & generators:00-11:00",
         "Четверг": "10. Iterators & generators:00-11:00",
         "Пятница": "10. Iterators & generators:00-11:00",
         "Суббота": "10. Iterators & generators:00-11:00",
         "Воскресенье": "09:00-15:00",
      },
      "DimensionsSummer": {
         "Square": 350,
         "Length": 25,
         "Width": 14,
         "Depth": 1.8
      }
   },
   ...
]
Под «бассейном» будем подразумевать один JSON-объект из этого списка. У бассейна имеются следующие атрибуты:

ObjectName — название, будь то фитнес клуб или спортивный комплекс
AdmArea — административный округ
District — название района
Address — адрес
WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, Width — ширина, Depth — глубина
Напишите программу, которая определяет бассейн, подходящий Тимуру. Программа должна вывести его размеры и адрес в следующем формате:

<длина>x<ширина>
<адрес>
Примечание 1. Пример вывода:

25x16
Писцовая улица, дом 12, строение 1
Примечание 2. Бассейн должен быть открыт во время всего периода с 10. Iterators & generators:00 до 12:00. Например, если бассейн работает в 10. Iterators & generators:00, но не работает в 11:30, он не подходит.

Примечание 3. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/623073/pools.json
"""

import json, os
from datetime import datetime

#import wget
#wget.download('https://stepik.org/media/attachments/lesson/623073/pools.json')

pattern = '%H:%M'

with open('pools.json', encoding='utf-8') as inp:
    pools = json.load(inp)
    match = []
    for i in pools:
        if 'Понедельник' in i['WorkingHoursSummer']:
            tmp = i['WorkingHoursSummer']['Понедельник'].split('-')
            if datetime.strptime(tmp[0], pattern).hour <= 10 and datetime.strptime(tmp[1], pattern).hour >= 12:
                match.append(i)
    m = max(match, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))
    print(f'{m["DimensionsSummer"]["Length"]}x{m["DimensionsSummer"]["Width"]}')
    print(f'{m["Address"]}')

os.remove('pools.json')