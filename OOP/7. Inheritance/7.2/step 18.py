"""
https://stepik.org/lesson/798678/step/18?unit=801641

Классы Triangle и EquilateralTriangle
Реализуйте класс Triangle, описывающий треугольник. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

a — длина стороны треугольника
b — длина стороны треугольника
c — длина стороны треугольника
Класс Triangle должен иметь один метод экземпляра:

perimeter() — метод, возвращающий периметр треугольника
Также реализуйте класс EquilateralTriangle, наследника класса Triangle, описывающий равносторонний треугольник. При создании экземпляра класс должен принимать один аргумент:

side — длина стороны треугольника
"""

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

class EquilateralTriangle(Triangle):

    def __init__(self, side):
       super().__init__(side, side, side)

