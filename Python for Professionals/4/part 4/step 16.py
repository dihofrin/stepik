"""
https://stepik.org/lesson/623073/step/16?unit=618703

Общественное питание 😰
Вам доступен файл food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях общественного питания:

[
   {
      "Name": "СМЕТАНА",
      "IsNetObject": "нет",
      "OperatingCompany": "",
      "TypeObject": "кафе",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Ярославский район",
      "Address": "город Москва, улица Егора Абакумова, дом 9",
      "SeatsCount": 48
   },
   ...
]
Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:

Name — название
IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
OperatingCompany — название сети
TypeObject — вид (кафе, столовая, ресторан и т.д.)
AdmArea — административная зона
District — район
Address — полный адрес
SeatsCount — количество посадочных мест
Напишите программу, которая определяет все виды заведений и для каждого вида находит самое большое заведение этого вида (имеет наибольшее количество посадочных мест). Программа должна вывести все виды заведений в лексикографическом порядке, указав для каждого самое большое заведение и количество посадочных мест в нем. Данные о заведениях должны быть расположены каждые на отдельной строке, в следующем формате:

<вид заведения>: <название заведения>, <количество посадочных мест>
Примечание 1. Начальная часть ответа выглядит так:

бар: Барное объединение ПРОФСОЮЗ, 800
буфет: СТОЛОВАЯ - КАНТИНАСИТИ, 320
закусочная: Бургерная FARШ, 74
...
Примечание 2. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/623073/food_services.json
"""

import json, os

#import wget
#wget.download('https://stepik.org/media/attachments/lesson/623073/food_services.json')



with open('food_services.json', encoding='utf-8') as file:
    r = json.load(file)
    types = {}
    for i in r:
        if i['TypeObject'] not in types:
            types[i['TypeObject']] = [i['Name'], i['SeatsCount']]
        else:
            if i['SeatsCount'] > types[i['TypeObject']][1]:
                types[i['TypeObject']] = [i['Name'], i['SeatsCount']]

    for i in sorted(types):
        print(f'{i}: {types[i][0]}, {types[i][1]}')
os.remove('food_services.json')