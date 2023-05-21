"""
https://stepik.org/lesson/802381/step/16?unit=805389


Класс Processor
Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.

Класс Processor имеет один статический метод:

process() — метод, который принимает в качестве аргумента произвольный объект, преобразует его в зависимости от его типа и возвращает полученный результат. Если тип переданного объекта не поддерживается методом, возбуждается исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod, чтобы он выполнял ту же задачу.

Примечание 1. Примеры преобразования объектов всех поддерживаемых типов показаны в методе process() класса Processor.
"""

from functools import singledispatchmethod


class Processor:

    @singledispatchmethod
    @staticmethod
    def process(obj):
        raise TypeError('Аргумент данного типа не поддерживается')

    @process.register(int, float)
    def process_digits(self, obj):
        return obj * 2

    @process.register(str)
    def process_strs(self, obj):
        return obj.upper()

    @process.register(list)
    def process_lists(self, obj):
        return sorted(obj)

    @process.register(tuple)
    def process_tuple(self, obj):
        return tuple(sorted(obj))