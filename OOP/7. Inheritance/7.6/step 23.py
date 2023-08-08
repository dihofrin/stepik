"""
https://stepik.org/lesson/841344/step/23?unit=844978

Функция get_method_owner()
Реализуйте функцию get_method_owner(), которая принимает два аргумента в следующем порядке:

cls — произвольный класс
method — строковое название метода
"""

def get_method_owner(cls, method):
    for cls in cls.mro():
        if method in cls.__dict__:
            return cls



