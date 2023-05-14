"""
https://stepik.org/lesson/801862/step/13?unit=804839

Класс Person
Вам доступен класс Person, описывающий человека. При создании экземпляра класс принимает два аргумента в следующем порядке:

name — имя человека
surname — фамилия человека
Экземпляр класса Person имеет два атрибута:

name — имя человека
surname — фамилия человека
Класс Person имеет одно свойство:

fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
<имя> <фамилия>
Реализуйте свойство fullname класса Person с помощью декоратора @property.

Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя. Аналогично при изменении полного имени должны изменяться имя и фамилия.
"""

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()
