"""
https://stepik.org/lesson/547172/step/19?unit=540798

Вам доступен набор различных файлов, названия которых представлены в списке file_names. Дополните приведенный ниже код, чтобы он создал архив files.zip и добавил в него все файлы из данного списка.

Примечание. Считайте, что файлы из списка file_names находятся в папке с программой.
"""

from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py','test.py']

with ZipFile('files.zip', mode='w') as file:
    for i in file_names:
        file.write(i)