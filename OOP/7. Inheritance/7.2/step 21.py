"""
https://stepik.org/lesson/798678/step/21?unit=801641

Класс FieldTracker🌶️🌶️
Реализуйте класс FieldTracker, наследники которого получают возможность отслеживать состояние определенных атрибутов своих экземпляров класса. Дочерние классы должны наследовать четыре метода экземпляра:

base() — метод, принимающий в качестве аргумента имя атрибута и возвращающий либо текущее значение этого атрибута, либо исходное (указанное при определении) значение этого атрибута, если оно было изменено
has_changed() — метод, принимающий в качестве аргумента имя атрибута и возвращающий True, если значение этого атрибута было изменено хотя бы раз, или False в противном случае
changed() — метод, возвращающий словарь, в котором ключами являются имена атрибутов, которые изменяли свои значения, а значениями — их исходные значения
save() — метод, сбрасывающий отслеживание. После вызова метода считается, что все атрибуты ранее не изменяли свои значения, а их текущие значения считаются исходными
Гарантируется, что наследники класса FieldTracker:

всегда имеют атрибут класса fields, содержащий кортеж с атрибутами, которые необходимо отслеживать
в своем инициализаторе всегда вызывают инициализатор класса FieldTracker после установки первичных значений отслеживаемым атрибутам
Примечание 1. Будем считать, что атрибут изменяет свое значение только в том случае, если устанавливаемое значение отличается от текущего.
"""

class FieldTracker:

    def __init__(self):
        self.changed_dict = {}

    def __setattr__(self, key, value):
        if key in self.__dict__ and key not in self.changed_dict:
            self.changed_dict[key] = self.__dict__[key]
        self.__dict__[key] = value

    def base(self, arg):
        if self.has_changed(arg):
            return self.changed_dict[arg]
        return self.__dict__[arg]

    def has_changed(self, arg):
        return arg in self.changed_dict

    def changed(self):
        return self.changed_dict

    def save(self):
        self.changed_dict = {}


