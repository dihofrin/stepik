"""
https://stepik.org/lesson/518491/step/11?unit=510939

При попытке выполнить приведенную ниже программу возникает ошибка. Найдите и исправьте ее, чтобы программа создала файл writing_test.csv, имеющий следующее содержание:

first_col,second_col
value1,value2
"""

import csv

with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
    columns = ['first_col', 'second_col']
    writer = csv.DictWriter(csv_file, fieldnames=columns)
    # записываем первую строку с названиями столбцов
    writer.writeheader()
    # записываем строку с данными
    writer.writerow({columns[0]: 'value1', columns[1]: 'value2'})