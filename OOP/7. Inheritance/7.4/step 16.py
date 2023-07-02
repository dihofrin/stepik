"""
https://stepik.org/lesson/860444/step/16?unit=864459

Класс DefaultList
Реализуйте класс DefaultList, наследника класса UserList, описывающий список, который при попытке получить элемент по несуществующему индексу возвращает значение по умолчанию. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса DefaultList. Если не передан, начальный набор элементов считается пустым
default — значение, возвращаемое при попытке получить элемент по несуществующему индексу. По умолчанию равняется None
Примечание 1. Экземпляр класса DefaultList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса DefaultList измениться  не должен.
"""

from collections import UserList

class DefaultList(UserList):

    def __init__(self, iterable=(), default=None):
        super().__init__(item for item in iterable)
        self.default = default

    def __getitem__(self, item):
        try:
            return self.data[item]
        except:
            return self.default

defaultlist = DefaultList()

print(defaultlist)