"""
https://stepik.org/lesson/805781/step/10?unit=808908

Класс Vector
Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

x — координата вектора по оси
�
x
y — координата вектора по оси
�
y
Экземпляр класса Vector должен иметь следующее формальное строковое представление:

Vector(<координата x>, <координата y>)
Также экземпляры класса Vector должны поддерживать между собой операции сложения и вычитания с помощью операторов + и - соответственно:

результатом сложения должен являться новый экземпляр класса Vector, координата по оси
�
x которого равна сумме координат по оси
�
x исходных векторов, координата по оси
�
y — сумме координат по оси
�
y исходных векторов
результатом вычитания должен являться новый экземпляр класса Vector координата по оси
�
x которого равна разности координат по оси
�
x исходных векторов с учетом порядка, координата по оси
�
y — разности координат по оси
�
y исходных векторов с учетом порядка
Наконец, экземпляр класса Vector должен поддерживать операции умножения и деления на число n с помощью операторов * и / соответственно:

результатом умножения должен являться новый экземпляр класса Vector, координаты которого умножены на n
результатом деления должен являться новый экземпляр класса Vector, координаты которого поделены на n
Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как вектор на число, так и число на вектор.

Примечание 1. Числами будем считать экземпляры классов int и float. Также будем гарантировать, что экземпляр класса Vector всегда делится на ненулевое число.

Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
"""

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}{self.x, self.y}'

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x / other, self.y / other)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __rmul__(self, other):
        return self.__mul__(other)
