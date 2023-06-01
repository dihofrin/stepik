"""
https://stepik.org/lesson/805783/step/10?unit=808910

Класс Vector

Реализуйте класс Vector, описывающий вектор на плоскости.
"""

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x, self.y}'

    def __bool__(self):
        return bool(self.x) or bool(self.y)

    def __int__(self):
        return int(self.__float__())

    def __float__(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def __complex__(self):
        return complex(self.x, self.y)