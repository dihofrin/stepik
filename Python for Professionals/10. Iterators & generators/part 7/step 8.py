"""
https://stepik.org/lesson/673155/step/8?unit=671418

Вам доступен файл data.csv, который содержит информацию об инвестициях в различные стартапы. В первом столбце записано название компании (стартапа), во втором — инвестируемая сумма в долларах, в третьем — раунд инвестиции:

company,raisedAmt,round
LifeLock,6850000,b
LifeLock,6000000,a
LifeLock,25000000,c
MyCityFaces,50000,seed
Flypaper,3000000,a
...
Напишите программу с использованием конвейеров генераторов, определяющую общую сумму, которая была инвестирована в раунде а, и выводящую полученный результат.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/673155/data.csv
"""

import csv
from wget import download

download('https://stepik.org/media/attachments/lesson/673155/data.csv')

with open('data.csv', 'r', encoding='utf-8') as file:
    header, *f = csv.reader(file)
    print(sum((int(line[1]) for line in f if line[2] == 'a')))
