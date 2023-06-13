"""
https://stepik.org/lesson/805786/step/19?unit=816645

Класс RandomLooper
Реализуйте класс RandomLooper. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом.

Экземпляр класса RandomLooper должен являться итератором, который генерирует в случайном порядке все элементы всех итерируемых объектов, переданных в конструктор, а затем возбуждает исключение StopIteration.

Примечание 1. Порядок элементов в возвращаемом итераторе необязательно должен совпадать с их порядком в тестовых данных.
"""

from random import shuffle
class RandomLooper:

    def __init__(self, *args):
        self.args = sum([list(a) for a in args], [])
        shuffle(self.args)


    def __iter__(self):
        return self

    def __next__(self):
        while self.args:
            return self.args.pop()
        raise StopIteration
