"""
https://stepik.org/lesson/810856/step/19?unit=816647

Класс RandomNumber
Реализуйте класс RandomNumber, описывающий дескриптор, который при обращении к атрибуту возвращает случайное целое число в заданном диапазоне. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

start — целое число
end — целое число
cache — булево значение, по умолчанию равняется False
Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать случайное целое число от start до end включительно. Если в качестве значения параметра cache при создании дескриптора было указано значение True, при каждом обращении к атрибуту дескриптор должен возвращать то число, которое было сгенерировано при первом обращении.

При установке или изменении значения атрибута дескриптор должен возбуждать исключение AttributeError с текстом:

Изменение невозможно
"""

from random import randint
class RandomNumber:

    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self.cached = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.output = randint(self.start, self.end)
        if self.cache:
            if not self.cached:
                self.cached = self.output
            return self.cached
        return self.output

    def __set__(self, instance, value):
        raise AttributeError('Изменение невозможно')

