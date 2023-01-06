"""
https://stepik.org/lesson/645394/step/8?unit=641995

Функция hash_as_key()
Реализуйте функцию hash_as_key(), которая принимает один аргумент:

objects — список хешируемых объектов
Функция должна возвращать словарь, ключом в котором является хеш-значение объекта из списка objects, а значением — сам объект. Если хеш-значения некоторых объектов совпадают, их следует объединить в список.

Примечание 1. Элементы в возвращаемом функцией словаре, а также объекты в списке, имеющие равные хеш-значения, должны располагаться в своем исходном порядке.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию hash_as_key(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.

Sample Input 1:

data = [1, 2, 3, 4, 5, 5]

print(hash_as_key(data))
Sample Output 1:

{1: 1, 2: 2, 3: 3, 4: 4, 5: [5, 5]}
Sample Input 2:

data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))
Sample Output 2:

{-2: [-1, -2], -3: -3, -4: -4, -5: -5}
Sample Input 3:

data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

print(hash_as_key(data))
Sample Output 3:

{11: 11, 22: 22, 33: 33, 44: 44, 55: 55, 66: 66, 77: 77, 88: 88, 99: 99, 111: 111}
"""

def hash_as_key(objects: list) -> dict:
    result = dict()
    for element in objects:
        if hash(element) not in result:
            result[hash(element)] = element
        elif not isinstance(result[hash(element)], list):
            result[hash(element)] = [result[hash(element)]] + [element]
        else:
            result[hash(element)].append(hash(element))
    return result