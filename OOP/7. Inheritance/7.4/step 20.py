"""
https://stepik.org/lesson/860444/step/20?unit=864459

Класс NumberList
Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList. Если хотя бы один элемент переданного итерируемого объекта не является числом, должно быть возбуждено исключение TypeError с текстом:
Элементами экземпляра класса NumberList должны быть числа
Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым
При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=) и методов append(), extend() и insert() должна производиться проверка на то, что добавляемые элементы являются числами, в противном случае должно возбуждаться исключение TypeError с текстом:

Элементами экземпляра класса NumberList должны быть числа
Примечание 1. Числами будет считать экземпляры классов int и float.

Примечание 2. Экземпляр класса NumberList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса NumberList измениться  не должен.
"""

from collections import UserList

class NumberList(UserList):

    def __init__(self, iterable=()):
        super().__init__(self.validate(item) for item in iterable)

    @staticmethod
    def validate(item):
        if isinstance(item, float | int):
            return item
        raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __add__(self, other):
        if isinstance(other, (type(self), list)):
            return super().__add__(self.validate(item) for item in other)
        return NotImplemented

    def __iadd__(self, other):
        super().__iadd__(self.validate(item) for item in other)
        return self


    def append(self, item):
        self.data.append(self.validate(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(self.validate(item) for item in other)