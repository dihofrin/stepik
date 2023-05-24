"""
https://stepik.org/lesson/805771/step/19?unit=808896

Класс Month
Реализуйте класс Month, описывающий месяц. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

year — год
month — порядковый номер месяца
Экземпляр класса Month должен иметь следующее формальное строковое представление:

Month(<год>, <порядковый номер месяца>)
И следующее неформальное строковое представление:

<год>-<порядковый номер месяца>
Также экземпляры класса Month должны поддерживать все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два Month объекта считаются равными, если их годы и порядковые номера месяцев совпадают. Month объект считается больше другого Month объекта, если его год больше. В случае если два Month объекта имеют равные года, большим считается тот, чей месяц больше. Методы, реализующие операции сравнения, должны уметь сравнивать как два Month объекта между собой, так и Month объект с кортежем из двух чисел, представляющих год и месяц.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
"""
from functools import total_ordering


@total_ordering
class Month:

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __repr__(self):
        return f'{self.__class__.__name__}{self.year, self.month}'

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __eq__(self, other):
        if isinstance(other, Month | tuple):
            return (self.year, self.month) == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month | tuple):
            return (self.year, self.month) < other
        return NotImplemented

