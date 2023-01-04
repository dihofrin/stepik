"""
https://stepik.org/lesson/623073/step/6?unit=618703

Элементы JSON
Напишите программу, которая принимает на вход описание одного объекта в формате JSON и выводит все пары ключ-значение этого объекта.

Формат входных данных
На вход программе подается корректное описание одного объекта в формате JSON.

Формат выходных данных
Программа должна вывести все пары ключ-значение введенного объекта, разделяя ключ и значение двоеточием, каждую на отдельной строке. Если значением ключа является список, то все его элементы должны быть выведены через запятую.

Примечание 1. Пары ключ-значение при выводе должны располагаться в своем исходном порядке.

Примечание 2. Для считывания произвольного числа строк используйте потоковый ввод sys.stdin.

Примечание 3. Тестовые данные доступны по ссылке.

Sample Input 1:

{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}
Sample Output 1:

size: 36
style: bold
name: text1
alignment: center
Sample Input 2:

{
 "type": "donut",
 "name": "Cake",
 "tastes": ["chocolate", "cream", "strawberry"]
}
Sample Output 2:

type: donut
name: Cake
tastes: chocolate, cream, strawberry
"""

import json, sys

d = json.loads(sys.stdin.read())
for key, value in d.items():
    if type(value) == list:
        print(f'{key}: {", ".join(str(i) for i in value)}')
    else:
        print(f'{key}: {value}')
