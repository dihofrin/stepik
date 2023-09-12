"""
https://stepik.org/lesson/864077/step/13?unit=923013

Класс MultiKeyDict 🌶️
Реализуйте класс MultiKeyDict, который практически во всем повторяет класс dict. Создание экземпляра класса MultiKeyDict должно происходить аналогично созданию экземпляра класса dict:

multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

print(multikeydict1['x'])        # 1
print(multikeydict2['z'])        # 3
Особенностью класса MultiKeyDict должен являться метод alias(), который должен позволять давать имеющимся ключам псевдонимы. Обращение по созданному псевдониму не должно ничем отличаться от обращения по оригинальному ключу, то есть с момента создания псевдонима у значения становится два ключа (или больше, если псевдонимов несколько):

multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')     # добавление ключу 'x' псевдонима 'z'
multikeydict.alias('x', 't')     # добавление ключу 'x' псевдонима 't'
print(multikeydict['z'])         # 100
multikeydict['t'] += 1
print(multikeydict['x'])         # 101

multikeydict.alias('y', 'z')     # теперь 'z' становится псевдонимом ключа 'y'
multikeydict['z'] += [30]
print(multikeydict['y'])         # [10, 20, 30]
Значение должно оставаться доступным по псевдониму даже в том случае, если оригинальный ключ был удален:

multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])         # 100
Ключи должны иметь приоритет над псевдонимами. Если некоторые ключ и псевдоним совпадают, то все операции при обращении к ним должны выполняться именно с ключом:

multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'y')
print(multikeydict['y'])         # [10, 20]
"""

from collections import UserDict

class MultiKeyDict(UserDict):

    def __init__(self, *args, **kwargs):
        self.aliases = {}
        super().__init__(*args, **kwargs)


    def alias(self, key, alias):
        self.aliases[alias] = key

    def __getitem__(self, item):
        if item in self.data:
            return self.data[item]
        return self.data[self.aliases[item]]


    def __setitem__(self, key, value):
        if key in self.aliases:
            self.data[self.aliases[key]] = value
        else:
            self.data[key] = value

    def __delitem__(self, key):
        if key in self.aliases.values():
            self.data['_' + key] = self.data[key]
            for k, v in self.aliases.items():
                if v == key:
                    self.aliases[k] = '_' + key
        del self.data[key]
