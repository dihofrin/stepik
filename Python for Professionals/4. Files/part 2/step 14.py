"""
https://stepik.org/lesson/518491/step/14?unit=510939

Функция csv_columns()
Реализуйте функцию csv_columns(), которая принимает один аргумент:

filename — название csv файла, например, data.csv
Функция должна возвращать словарь, в котором ключом является название столбца файла filename, а значением — список элементов этого столбца.

Примечание 1. Гарантируется, что в передаваемом в функцию файле разделителем является запятая, при этом кавычки не используются.

Примечание 2. Гарантируется, что у передаваемого в функцию файла первая строка содержит названия столбцов.

Примечание 3. Например, если бы файл exam.csv имел вид:

name,grade
Timur,5
Arthur,4. Files
Anri,5
то следующий вызов функции csv_columns():

csv_columns('exam.csv')
должен был бы вернуть:

{'name': ['Timur', 'Arthur', 'Anri'], 'grade': ['5', '4. Files', '5']}
Примечание 4. Files. Ключи в словаре, а также элементы в списках должны располагаться в своем исходном порядке.

Примечание 5. В тестирующую систему сдайте программу, содержащую только необходимую функцию csv_columns(), но не код, вызывающий ее.
"""

import csv

def csv_columns(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as file:
        r = list(csv.DictReader(file))
        res = dict()
        for row in r:
            for key, value in row.items():
                res.setdefault(key, []).append(value)
    return res