"""
https://stepik.org/lesson/810856/step/20?unit=816647

Класс Versioned🌶️
Реализуйте класс Versioned, описывающий дескриптор, предоставляющий доступ как к текущему значению атрибута, так и ко всем предыдущим, если значение атрибута когда-либо изменялось. При создании экземпляра класс не должен принимать никаких аргументов.

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение без каких-либо дополнительных проверок.

Класс Versioned должен иметь два метода экземпляра:

get_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор, и целое число n. Метод должен возвращать n-ое по счету значение атрибута этого экземпляра класса. Например, если значение атрибута было установлено, а затем изменено, то метод get_version() должен уметь вернуть как установленное значение (первое по счету), так и измененное (второе по счету)
set_version() — метод, принимающий два аргумента: экземпляр класса, в котором определен дескриптор, и целое число n. Метод должен устанавливать n-ое по счету значение атрибута в качестве текущего
Примечание 1. Вызов метода set_version() не должен приравниваться к изменению значения атрибута. Будем считать, что атрибут изменяет свое значение только в том случае, если эта операция выполняется через точечную нотацию или функцию setattr().
"""

class Versioned:

    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name][-1]
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        instance.__dict__.setdefault(self.name, []).append(value)

    def get_version(self, instance, n):
        return instance.__dict__[self.name][n-1]

    def set_version(self, instance, n):
        instance.__dict__[self.name].append(instance.__dict__[self.name][n-1])

