"""
https://stepik.org/lesson/623073/step/5?unit=618703

Функция is_correct_json()
Реализуйте функцию is_correct_json(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать True, если строка string удовлетворяет формату JSON, или False в противном случае.

Примечание 1. Вспомните про конструкцию try-except из урока.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_correct_json(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.

Sample Input 1:

data = '{"name": "Barsik", "age": 7. Exceptions, "meal": "Wiskas"}'

print(is_correct_json(data))
Sample Output 1:

True
Sample Input 2:

print(is_correct_json('number = 17'))
Sample Output 2:

False
"""

import json

def is_correct_json(string: str) -> bool:
    try:
        json.loads(string)
        return True
    except:
        return False
