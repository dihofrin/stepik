"""
https://stepik.org/lesson/801862/step/15?unit=804839

Класс QuadraticPolynomial

"""

class QuadraticPolynomial:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    @property
    def x1(self):
        if (self.b * self.b - 4 * self.a * self.c) < 0:
            return None
        return (-self.b - (self.b * self.b - 4 * self.a * self.c) ** 0.5) / (self.a * 2)

    @property
    def x2(self):
        if (self.b * self.b - 4 * self.a * self.c) < 0:
            return None
        return (-self.b + (self.b * self.b - 4 * self.a * self.c) ** 0.5) / (self.a * 2)

    @property
    def view(self):
        result = ''
        if self.a < 0:
            result = '-' + f'{abs(self.a)}x^2'
        else:
            result = f'{abs(self.a)}x^2'
        if self.b < 0:
            result = result + ' - ' + f'{abs(self.b)}x'
        else:
            result = result + ' + ' + f'{abs(self.b)}x'
        if self.c < 0:
            result = result + ' - ' + f'{abs(self.c)}'
        else:
            result = result + ' + ' + f'{abs(self.c)}'
        return result

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, values):
        self.a, self.b, self.c = values
        return self.a, self.b, self.c

