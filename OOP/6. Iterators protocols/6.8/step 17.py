"""
https://stepik.org/lesson/810856/step/17?unit=816647

Класс LimitedTakes
Реализуйте класс LimitedTakes, описывающий дескриптор, который позволяет получать значение атрибута лишь определенное количество раз. При создании экземпляра класс должен принимать один аргумент:

times — количество доступных обращений к атрибуту
Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
Если к атрибуту было выполнено times обращений, во время всех последующих обращений должно возбуждаться исключение MaxCallsException с текстом:

Превышено количество доступных обращений
При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение без каких-либо дополнительных проверок.
"""


class MaxCallsException(Exception):
    pass

class LimitedTakes:

    def __set_name__(self, owner, name):
        self._name = name

    def __init__(self, times):
        self.times = times

    def __get__(self, instance, owner):
        if self._name not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        if self.times < 1:
            raise MaxCallsException ('Превышено количество доступных обращений')
        self.times -= 1
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
