"""
https://stepik.org/lesson/794484/step/17?unit=797232

Функция pluck()
Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:

data — словарь произвольной вложенности
path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность ключей, например, key1.key2, то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1]. Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, функция должна вернуть значение default.

"""

def pluck(data, path, default=None):
    path = path.split('.')
    for i in range(len(path)):
        if i == len(path) - 1:
            if path[i] in data:
                return data[path[i]]
        if path[i] in data.keys():
            if isinstance(data[path[i]], dict):
                data = data[path[i]]
            else:
                return data[path[i]]
        else:
            return default

