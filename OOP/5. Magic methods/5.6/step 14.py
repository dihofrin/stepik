"""
https://stepik.org/lesson/805787/step/14?unit=808914

Класс Filter
Реализуйте класс Filter, описывающий объект для фильтрации элементов итерируемых объектов. При создании экземпляра класс должен принимать один аргумент:

predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Экземпляр класса Filter должен являться вызываемым объектом и принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса Filter должен возвращать список, элементами которого являются элементы итерируемого объекта iterable, для которых функция predicate вернула значение True.
"""

class Filter:

    def __init__(self, predicate):
        self.predicate = predicate

    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))
