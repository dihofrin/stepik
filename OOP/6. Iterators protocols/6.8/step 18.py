"""
https://stepik.org/lesson/810856/step/18?unit=816647

Класс TypeChecked
Реализуйте класс TypeChecked, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута принадлежит определенному типу данных. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является типом данных.

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен проверять, принадлежит ли это значение одному из типов, указанных при создании дескриптора. Если значение не принадлежит ни одному из типов, должно быть возбуждено исключение TypeError с текстом:

Некорректное значение
"""

class TypeChecked:

    def __init__(self, *args):
        self.args = args

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if type(value) in self.args:
            instance.__dict__[self.name] = value
        else:
            raise TypeError('Некорректное значение')

