"""
https://stepik.org/lesson/805771/step/20?unit=808896

Класс Version
Реализуйте класс Version, описывающий версию программного обеспечения. При создании экземпляра класс должен принимать один аргумент:

version — строка из трех целых чисел, разделенных точками и описывающих версию ПО. Например, 2.8.1. Если одно из чисел не указано, оно считается равным нулю. Например, версия 2 равнозначна версии 2.0.0, а версия 2.8 равнозначна версии 2.8.0
Экземпляр класса Version должен иметь следующее формальное строковое представление:

Version('<версия ПО в виде трех целых чисел, разделенных точками>')
И следующее неформальное строковое представление:

<версия ПО в виде трех целых чисел, разделенных точками>
Также экземпляры класса Version должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два Version объекта считаются равными, если все три числа в их версиях совпадают. Version объект считается больше другогоVersion объекта, если первое число в его версии больше. Или если второе число в его версии больше, если первые числа совпадают. Или если третье число в его версии больше, если первые и вторые числа совпадают.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
"""

from functools import total_ordering

@total_ordering
class Version:

    def __init__(self, version):
        self.version = version.split('.')
        self.a = self.b = self.c = None
        if len(self.version) == 3:
            self.a, self.b, self.c = self.version
        if len(self.version) == 2:
            self.a = int(self.version[0])
            self.b = int(self.version[1])
            self.c = 0
        if len(self.version) == 1:
            self.a = int(self.version[0])
            self.b = 0
            self.c = 0
        self.version = tuple(map(int, (self.a, self.b, self.c)))

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.value())})'

    def value(self):
        return ".".join(map(str, self.version))

    def __str__(self):
        return self.value()

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version == other.version
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.version < other.version
        return NotImplemented
