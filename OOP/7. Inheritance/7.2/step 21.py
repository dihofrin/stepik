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

    def base(self, arg):
        return self.__dicta__[arg]

    def has_changed(self, arg=False):
        return arg

    def changed(self):
        return self.__dict__

    def save(self):
        return self
