"""
https://stepik.org/lesson/518491/step/15?unit=510939

Популярные домены
Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса. В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих данный домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, при совпадении количества использований — в лексикографическом порядке.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. https://stepik.org/media/attachments/lesson/518491/data.csv

Примечание 3. Начальная часть файла domain_usage.csv выглядит так:

domain,count
rambler.ru,24
iCloud.com,29
...
Примечание 4. Files. При открытии файла используйте явное указание кодировки UTF-8.
"""

import csv, os

#wget.download('https://stepik.org/media/attachments/lesson/518491/data.csv')

with open('data.csv', 'r', encoding='utf-8') as file:
    data = list(csv.reader(file))[1:]
    d = dict()
    for row in data:
        domain = row[2].split('@')[1]
        d[domain] = d.get(domain, 0) + 1
    with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as output_file:
            columns = ['domain', 'count']
            writer = csv.writer(output_file)
            writer.writerow(columns)
            for i in sorted(d, key=lambda x: (d[x], x)):
                row = [i, d[i]]
                writer.writerow(row)
os.remove('data.csv')