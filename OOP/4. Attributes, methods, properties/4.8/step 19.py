"""
https://stepik.org/lesson/802381/step/19?unit=805389

Класс BirthInfo 🌶️
Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать один аргумент:

birth_date — дата рождения, представленная в одном из следующих вариантов:
экземпляр класса date
строка с датой в ISO формате
список или кортеж из трех целых чисел: года, месяца и дня
Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено исключение TypeError с текстом:

Аргумент переданного типа не поддерживается
Экземпляр класса BirthInfo должен иметь один атрибут:

birth_date — дата рождения в виде экземпляра класса date
Класс BirthInfo должен иметь одно свойство:

age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет, прошедших с даты рождения на сегодняшний день
Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения его возраст увеличивается на один год.

Приведенный ниже код:

birthinfo = BirthInfo(date(2023, 2, 26))

print(birthinfo.age)
в 2024-02-25 должен выводить:

0
в 2024-02-26 должен выводить:

1
в 2025-02-25 должен выводить:

1
 в 2025-02-26 должен выводить:

2
Примечание 2. Для проверки того, что свойство age возвращает верный возраст, мы используем собственную функцию current_age(), которая вычисляет возраст в годах на основе даты рождения и текущей даты.
"""

from functools import singledispatchmethod
from datetime import date, datetime

class BirthInfo:

    @singledispatchmethod
    def __init__(self, birth_date):
        self.birth_date = birth_date
        self.year = self.month = self.day = None
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def date_init(self, birth_date):
        self.birth_date = birth_date


    @__init__.register(str)
    def str_init(self, birth_date):
        self.birth_date = date.fromisoformat(birth_date)


    @__init__.register(tuple)
    @__init__.register(list)
    def init(self, birth_date):
        self.year, self.month, self.day = birth_date
        self.birth_date = date(self.year, self.month, self.day)

    @property
    def age(self):
        curr = datetime.now().date()
        bd = self.birth_date
        if curr.month < bd.month or curr.day < bd.day:
            return curr.year - bd.year - 1
        else:
            return curr.year - bd.year



