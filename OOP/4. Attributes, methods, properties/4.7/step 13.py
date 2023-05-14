"""
https://stepik.org/lesson/794698/step/13?unit=797450

Класс QuadraticPolynomial
"""

class QuadraticPolynomial:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, arg):
        return cls(*arg)

    @classmethod
    def from_str(cls, s):
        return cls(*map(float, s.split()))

