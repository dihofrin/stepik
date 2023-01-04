"""
https://stepik.org/lesson/547172/step/15?unit=540798

Объем файлов
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах, в следующем формате:

Объем исходных файлов: <объем до сжатия> байт(а)
Объем сжатых файлов: <объем после сжатия> байт(а)
Примечание 1. Вывод на примере архива test.zip из конспекта:

Объем исходных файлов: 7810260 байт(а)
Объем сжатых файлов: 7798267 байт(а)
Примечание 2. Указанный архив доступен по ссылке https://stepik.org/media/attachments/lesson/547172/workbook.zip
"""

from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    info = file.infolist()
    compressed = 0
    source = 0
    for i in info:
        compressed += i.compress_size
        source += i.file_size
    print(f'Объем исходных файлов: {source} байт(а)')
    print(f'Объем сжатых файлов: {compressed} байт(а)')