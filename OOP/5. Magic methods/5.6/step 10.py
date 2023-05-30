"""
https://stepik.org/lesson/805787/step/10?unit=808914

Класс RaiseTo
Реализуйте класс RaiseTo, экземпляры которого позволяют возводить числа в фиксированную степень. При создании экземпляра класс должен принимать один аргумент:

degree — показатель степени
Экземпляр класса RaiseTo должен являться вызываемым объектом и принимать один аргумент:

x — число
Экземпляр класса RaiseTo должен возвращать значение x в степени degree.
"""

class RaiseTo:

    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x):
        return x ** self.degree

