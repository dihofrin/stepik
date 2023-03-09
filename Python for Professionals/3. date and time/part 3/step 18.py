"""
https://stepik.org/lesson/611754/step/18?unit=607091

Дневник космонавта 🌶️
Вам доступен текстовый файл diary.txt, в который космонавт записывал небольшие отчёты за день. Каждый новый отчёт он мог записать либо в начало файла, либо в середину, либо в конец. Все отчеты разделены между собой пустой строкой. Каждый новый отчёт начинается со строки с датой и временем в формате DD.MM.YYYY; HH:MM, после которой следуют события, произошедшие за указанный день:

29.04.2006; 06:55
It wasn’t until several hours after launch that we were able to take the time to get out of our seats and enter the “habitation module.”
Then, after another orbital maneuver, we finally were able to take a several hour break and get a little sleep.

03.05.2006; 20:24
Everybody had a sleeping bag although I only used mine on a couple of brief occasions, and then only when getting a little chilly.

...
Напишите программу, которая расставляет все записи космонавта в хронологическом порядке и выводит полученный результат.
"""
import os

from wget import download
from datetime import datetime

download('https://stepik.org/media/attachments/lesson/611754/diary.txt')
pattern = "%d.%m.%Y; %H:%M"

with open('diary.txt', 'r', encoding='utf-8') as file:
    s = file.read().split('\n\n')
    d = {datetime.timestamp(datetime.strptime(i[:17], pattern)):i[18:] for i in s}
    sorted_keys = sorted(d)
    for k in sorted_keys:
        print(datetime.fromtimestamp(k).strftime(pattern), d[k], sep='\n', end='\n\n')

os.remove('diary.txt')
