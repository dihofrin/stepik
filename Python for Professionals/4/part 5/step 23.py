"""
https://stepik.org/lesson/547172/step/23?unit=540798

Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу, которая выводит его файловую структуру и объем каждого файла.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде. Так как архив имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.

Примечание 1. Вывод на примере архива test.zip из конспекта:

test
  Картинки
    1.jpg 88 KB
    avatar.png 19 KB
    certificate.png 43 KB
    py.png 33 KB
    World_Time_Zones_Map.png 2 MB
    Снимок экрана.png 11 KB
  Неравенства.djvu 5 MB
  Программы
    image_util.py 5 KB
    sort.py 61 B
  Разные файлы
    astros.json 505 B
Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.

Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
Примечание 4. Указанный архив доступен по ссылке https://stepik.org/media/attachments/lesson/547172/desktop.zip
"""

from zipfile import ZipFile

def get_zize(size):
    if size < 1025:
        return str(size) + ' B'
    if 1024 < size < 1024 * 1024:
        return str(round(size/1024)) + ' KB'
    if 1024*1024 < size < 1024 * 1024 * 1024:
        return str(round(size/1024/1024)) + ' MB'

with ZipFile('desktop.zip') as file:
    i = file.infolist()
    for i in i:
        if not i.is_dir():
            print(i.filename.count('/') * '  ' + i.filename.split('/')[-1], get_zize(i.file_size))
        else:
            print('  ' * (i.filename.count('/') - 1) + i.filename.split('/')[i.filename.count('/') - 1])