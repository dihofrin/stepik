"""
https://stepik.org/lesson/673155/step/11?unit=671418

Функция txt_to_dict()
Вам доступен файл planets.txt, содержащий информацию о различных планетах. В первых четырех строках указаны характеристики первой планеты, после чего следует пустая строка, затем характеристики второй планеты, и так далее:

Name = Mercury
Diameter = 4879.4
Mass = 3.302×10^23
OrbitalPeriod = 0.241

Name = Venus
Diameter = 12103.6
Mass = 4.869×10^24
OrbitalPeriod = 0.615

...
Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий последовательность словарей, каждый из которых содержит информацию об очередной планете из файла planets.txt, а именно ее название, диаметр, массу и орбитальный период. Например:

{'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
Примечание 1. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/673155/planets.txt
"""

from wget import download
download('https://stepik.org/media/attachments/lesson/673155/planets.txt')
def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        planets = file.read().split('\n\n')
        planets2 = (line.split('\n') for line in planets)
        planets3 = ([i.split(' = ') for i in line] for line in planets2)
        for i in planets3:
            tmp = {}
            for j in i:
                tmp.update({j[0]: j[1]})
            yield tmp
