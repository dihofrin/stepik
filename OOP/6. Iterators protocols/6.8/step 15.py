"""
https://stepik.org/lesson/810856/step/15?unit=816647

Класс NonKeyword
Реализуйте класс NonKeyword, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута не является строковым ключевым словом в Python. При создании экземпляра класс должен принимать один аргумент:

name — имя атрибута, за которым будет закреплен дескриптор
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, не является ли это значение строковым ключевым словом в Python. Если значение является строковым ключевым словом, должно быть возбуждено исключение ValueError с текстом:

Некорректное значение
"""

from keyword import kwlist
class NonKeyword:

    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        if self.name in obj.__dict__:
            return obj.__dict__[self.name]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if value not in kwlist:
            obj.__dict__[self.name] = value
        else:
            raise ValueError('Некорректное значение')
