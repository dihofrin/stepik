"""
https://stepik.org/lesson/805770/step/14?unit=808895

Класс Rectangle
Вам доступен класс Rectangle, описывающий прямоугольник. При создании экземпляра класс принимает два аргумента в следующем порядке:

length — длина прямоугольника
width — ширина прямоугольника
Реализуйте для экземпляров класса Rectangle следующее формальное и неформальное строковое представление:

Rectangle(<длина прямоугольника>, <ширина прямоугольника>)
"""

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'