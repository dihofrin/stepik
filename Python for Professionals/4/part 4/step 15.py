"""
https://stepik.org/lesson/623073/step/15?unit=618703

Общественное питание 😥
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
SeatsCount — количество мест
Напишите программу, которая:

определяет район Москвы, в котором находится больше всего заведений, и выводит название этого района и количество заведений в нем
определяет сеть с самым большим числом заведений и выводит название этой сети и количество заведений этой сети
Полученные значения программа должна вывести в следующем формате:

<район>: <количество заведений>
<название сети>: <количество заведений>
Примечание 1. Гарантируется, что искомая сеть единственная.

Примечание 2. Пример вывода:

район Метрогородок: 456
Французская пекарня SeDelice: 144
Примечание 3. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/623073/food_services.json
"""

import json, os

#import wget
#wget.download('https://stepik.org/media/attachments/lesson/623073/food_services.json')


with open('food_services.json', encoding='utf-8') as file:
    r = json.load(file)
    nets = []
    n_dict = {}
    distrs = {}
    for i in r:
        distrs[i['District']] = distrs.get(i['District'], 0) + 1
        if i['IsNetObject'] == 'да':
            nets.append(i)

    for i in nets:
        n_dict[i['OperatingCompany']] = n_dict.get(i['OperatingCompany'], 0) + 1

    max_district = max(distrs, key=lambda x: distrs[x])
    max_nets = max(n_dict, key=lambda x: n_dict[x])


    print(f'{max_district}: {distrs[max_district]}')
    print(f'{max_nets}: {n_dict[max_nets]}')
os.remove('food_services.json')