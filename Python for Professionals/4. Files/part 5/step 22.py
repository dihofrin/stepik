"""
https://stepik.org/lesson/547172/step/22?unit=540798

Шахматы были лучше 🌶️
Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
У футболиста имеются следующие атрибуты:

first_name — имя
last_name — фамилия
team — название футбольного клуба
position — игровая позиция
Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.

Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным текстовым файлом в формате JSON. Для того чтобы определить, является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего урока.

Примечание 2. Начальная часть ответа выглядит так:

Alex Iwobi
Alexis Sanchez
...
Примечание 3. Указанный архив доступен по ссылке https://stepik.org/media/attachments/lesson/547172/data.zip
"""

from zipfile import ZipFile
import json

with ZipFile('data.zip') as file:
    i = file.infolist()
    result = []
    for i in i:
        if not i.is_dir():
            if i.filename.endswith('.json'):
                try:
                    with file.open(i.filename.encode('cp437').decode('cp866')) as f:
                        s = json.load(f)
                        if s['team'] == 'Arsenal':
                            result.append([s['first_name'], s['last_name']])
                except:
                    pass
    for i in sorted(result, key=lambda x: x[0]):
        print(*i)