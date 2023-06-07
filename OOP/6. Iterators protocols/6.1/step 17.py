"""
https://stepik.org/lesson/805786/step/17?unit=816645

Класс AttrsIterator
Реализуйте класс AttrsIterator. При создании экземпляра класс должен принимать один аргумент:

obj — произвольный объект
Экземпляр класса AttrsIterator должен являться итератором, который генерирует все атрибуты объекта obj в виде кортежей из двух элементов, первый из которых представляет имя атрибута, второй — значение атрибута.

Примечание 1. Порядок атрибутов при генерации должен совпадать с их порядком в словаре атрибутов __dict__.
"""

class AttrsIterator:

    def __init__(self, obj):
        self._obj = list(obj.__dict__.items())
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self._obj):
            raise StopIteration
        return self._obj[self.start]


