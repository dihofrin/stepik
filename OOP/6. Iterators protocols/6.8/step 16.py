"""
https://stepik.org/lesson/810856/step/16?unit=816647

Класс NonNegativeInteger
Реализуйте класс NonNegativeInteger, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута является неотрицательным целым числом. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя атрибута, за которым будет закреплен дескриптор
default — значение по умолчанию. Если не передан, имеет значение None
При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение не установлено, должно возвращаться значение по умолчанию, указанное при создании дескриптора. Если значение по умолчанию равняется None, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, является ли это значение неотрицательным целым числом. Если значение не является неотрицательным целым числом, должно быть возбуждено исключение ValueError с текстом:

Некорректное значение
"""


class NonNegativeInteger:

    def __init__(self, name, default=None):
        self._name = name
        self.default = default

    def __get__(self, instance, owner):
        if self._name in instance.__dict__:
            return instance.__dict__[self._name]
        elif self.default is not None:
            instance.__dict__[self._name] = self.default
            return instance.__dict__[self._name]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, owner, value):
        if isinstance(value, int) and value > -1:
            owner.__dict__[self._name] = value
        else:
            raise ValueError('Некорректное значение')
