"""
https://stepik.org/lesson/518491/step/19?unit=510939

Сортировка по столбцу 🌶️
Вам доступен файл deniro.csv, каждый столбец которого содержит либо только числа, либо только слова:

Machete,2010,72
Marvin's Room,1996,80
Raging Bull,1980,97
...
Напишите программу, которая сортирует содержимое данного файла по указанному столбцу. Причем данные должны быть отсортированы в порядке возрастания чисел, если столбец содержит числа, и в лексикографическом порядке слов, если столбец содержит слова.

Формат входных данных
На вход программе подается натуральное число — номер столбца файла deniro.csv.

Формат выходных данных
Программа должна отсортировать содержимое файла deniro.csv по введенному столбцу и вывести полученный результат в исходном формате.

Примечание 1. Нумерация столбцов начинается с единицы.

Примечание 2. Например, если бы файл deniro.csv имел вид:

red,4. Files
blue,3
green,28
purple,1
и его требовалось отсортировать по второму столбцу (в порядке возрастания чисел), то программа должна была бы вывести:

purple,1
blue,3
red,4. Files
green,28
Примечание 3. Если две какие-либо строки имеют одинаковые значения в столбцах, то следует сохранить их исходный порядок следования.

Примечание 4. Files. Разделителем в файле deniro.csv является запятая, при этом кавычки не используются.

Примечание 5. Указанный файл доступен по ссылке. https://stepik.org/media/attachments/lesson/518491/deniro.csv
"""

import csv, os

#import wget
#wget.download('https://stepik.org/media/attachments/lesson/518491/deniro.csv')

col = int(input())


with open('deniro.csv', 'r', encoding='utf-8') as file:
    data = list(csv.reader(file))
    s = dict()
    for i in range(len(data)):
        s[i] = data[i]
    if s[0][col-1].isdigit():
        for value in sorted(s.values(), key=lambda item: int(item[col-1])):
            print(*value, sep=',')
    else:
        for values in sorted(s.values()):
            print(*values, sep=',')
os.remove('deniro.csv')