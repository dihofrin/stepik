"""
https://stepik.org/lesson/802381/step/18?unit=805389

Класс Formatter
Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Formatter должен иметь один статический метод:

format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий информацию о переданном объекте в формате, зависящем от его типа. Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.

Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.
"""

from functools import singledispatchmethod

class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(*args):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @format.register(float)
    @staticmethod
    def format_digit(obj):
        if isinstance(obj, int):
            print(f'Целое число: {obj}')
        else:
            print(f'Вещественное число: {obj}')

    @format.register(list)
    @format.register(tuple)
    @staticmethod
    def format_coll(obj):
        output = ''
        if isinstance(obj, list):
            output += 'Элементы списка: '
        else:
            output += 'Элементы кортежа: '
        print(output, end='')
        print(*obj, sep=', ')

    @format.register(dict)
    @staticmethod
    def format_dict(obj):
        print('Пары словаря: ', end='')
        print(*obj.items(), sep=', ')