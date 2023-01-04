"""
https://stepik.org/lesson/584474/step/14?unit=579234

Ты не пройдешь
Реализуйте функцию filter_dump(), которая принимает три аргумента в следующем порядке:

filename — название pickle файла, например, data.pkl
objects — список произвольных объектов
typename — тип данных
Функция должна создавать pickle файл с названием filename, который содержит сериализованный список только тех объектов из списка objects, тип которых равен typename.

Примечание 1. Например, вызов функции filter_dump() следующим образом:

filter_dump('numbers.pkl', [1, '2', 3, 4. Files, '5'], int)
должен создавать файл numbers.pkl, содержащий сериализованный список [1, 3, 4. Files].

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_dump(), но не код, вызывающий ее.
"""

import pickle

def filter_dump(filename, object, typename):
    with open(filename, 'wb') as file:
        pickle.dump([i for i in object if type(i)==typename], file)