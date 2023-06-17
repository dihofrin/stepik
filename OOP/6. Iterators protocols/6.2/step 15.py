"""
https://stepik.org/lesson/805785/step/15?unit=816644

Класс AttrDict
Реализуйте класс AttrDict, описывающий упрощенный словарь, значения элементов которого можно получать как по ключам ([key]), так и по одноименным атрибутам (.key). При создании экземпляра класс должен принимать один аргумент:

data — словарь, определяющий начальный набор элементов упрощенного словаря. Если не передан, начальный набор элементов считается пустым
При передаче экземпляра класса AttrDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса AttrDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.

Наконец, экземпляр класса AttrDict должен позволять получать значения своих элементов как по их ключам, так и по одноименным атрибутам. Реализовывать добавление элементов и изменение их значений по одноименным атрибутам не нужно.

Примечание 1. Экземпляр класса AttrDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса AttrDict измениться  не должен.
"""
from copy import deepcopy
class AttrDict:

    def __init__(self, data=None):
        if data:
            self.__dict__ = data

    def __getattr__(self, item):
        if item not in self.data:
            raise AttributeError
        return self.data[item]

    def __iter__(self):
        yield from self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __setitem__(self, key, item):
        if key not in self.__dict__:
            self.__dict__[key] = item

    def __getitem__(self, item):
        return self.__dict__[item]



d = AttrDict()
d.name = 'Leonardo da Vinci'

try:
    print(d['name'])
except KeyError:
    print('Ключ отсутствует')