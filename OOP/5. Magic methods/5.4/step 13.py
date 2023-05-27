"""
https://stepik.org/lesson/805932/step/13?unit=809059

Класс ColoredPoint
Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

x — координата точки по оси
�
x
y — координата точки по оси
�
y
color — цвет в формате RGB, представленный кортежем из трех целых чисел в диапазоне [0; 255], по умолчанию имеет значение (0, 0, 0)
Экземпляр класса ColoredPoint должен иметь три атрибута:

x — координата точки по оси
�
x
y — координата точки по оси
�
y
color — цвет в формате RGB, представленный кортежем из трех целых чисел от 0 до 255
Также экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:

ColoredPoint(<координата x>, <координата y>, <цвет точки в виде трехэлементного кортежа>)
И следующее неформальное строковое представление:

(<координата x>, <координата y>)
Наконец, экземпляр класса ColoredPoint должен поддерживать унарные операторы +, - и ~:

результатом унарного + должен являться новый экземпляр класса ColoredPoint c исходными координатами и цветом
результатом унарного - должен являться новый экземпляр класса ColoredPoint c координатами, умноженными на минус единицу, и исходным цветом
результатом унарного ~ должен являться новый экземпляр класса ColoredPoint c координатами, переставленными местами, и инвертированным цветом: значение каждой компоненты цвета отнимается от 255
"""

class ColoredPoint:

    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f'{self.x, self.y}'

    def __repr__(self):
        return f'{self.__class__.__name__}{self.x, self.y, self.color}'

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)

    def __invert__(self):
        return ColoredPoint(self.y, self.x, tuple(255-c for c in self.color))