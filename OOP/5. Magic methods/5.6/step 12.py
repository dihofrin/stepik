"""
https://stepik.org/lesson/805787/step/12?unit=808914

 Класс QuadraticPolynomial
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
"""

class QuadraticPolynomial:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x * x + self.b * x + self.c

