"""
https://stepik.org/lesson/802381/step/17?unit=805389

Класс Negator
Реализуйте класс Negator. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Negator должен иметь один статический метод:

neg() — метод, принимающий в качестве аргумента объект и возвращающий его противоположное значение. Если методу передается целое или вещественное число, он должен возвращать это число, взятое с противоположным знаком. Если методу в качестве аргумента передается булево значение, он должен возвращать булево значение, противоположное переданному. Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
"""

from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(obj):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def neg_digit(obj):
        return -obj

    @neg.register(bool)
    @staticmethod
    def neg_bool(obj):
        return not obj