"""
https://stepik.org/lesson/906773/step/14?unit=912312

Класс Const
Реализуйте класс Const. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Класс Const должен разрешать устанавливать атрибуты своим экземплярам и получать их значения, но не разрешать изменять значения этих атрибутов, а также удалять их. При попытке изменить значение атрибута должно возбуждаться исключение AttributeError с текстом:

Изменение значения атрибута невозможно
При попытке удалить атрибут должно возбуждаться исключение AttributeError с текстом:

Удаление атрибута невозможно
"""

class Const:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value
        else:
            raise AttributeError('Изменение значения атрибута невозможно')


    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')