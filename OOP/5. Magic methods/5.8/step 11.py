"""
https://stepik.org/lesson/906773/step/11?unit=912312

Класс DefaultObject
Реализуйте класс DefaultObject. При создании экземпляра класс должен принимать один именованный аргумент default, имеющий значение по умолчанию None, а после произвольное количество именованных аргументов. Аргументы, передаваемые после default, должны устанавливаться создаваемому экземпляру в качестве атрибутов.

При обращении к несуществующему атрибуту экземпляра класса DefaultObject должно возвращаться значение default.
"""

class DefaultObject:

    def __init__(self, default=None, **kwargs):
        self.__dict__ = {**kwargs}
        self.default = default

    def __getattr__(self, item):
        return self.default
