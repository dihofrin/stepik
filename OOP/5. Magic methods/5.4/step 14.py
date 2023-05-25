"""
https://stepik.org/lesson/805932/step/14?unit=809059

Класс Matrix🌶️🌶️
Реализуйте класс Matrix, описывающий двумерную матрицу. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

rows — количество строк в матрице
cols — количество столбцов в матрице
value — начальное значение для элементов матрицы, по умолчанию имеет значение 0
Класс Matrix должен иметь два метода экземпляра:

get_value() — метод, принимающий в качестве аргументов строку row и столбец col и возвращающий элемент матрицы со строкой row и столбцом col
set_value() — метод, принимающий в качестве аргументов строку row, столбец col и значение value и устанавливающий в качестве значения элемента матрицы со строкой row и столбцом col значение value
Экземпляр класса Matrix должен иметь следующее формальное строковое представление:

Matrix(<количество строк в матрице>, <количество столбцов в матрице>)
Неформальным строковым представлением должна быть строка, в которой перечислены все элементы матрицы. Элементы строки матрицы должны быть разделены пробелом, строки матрицы должны быть разделены символом переноса строки \n. Например, для объекта Matrix(2, 3) неформальным строковым представлением должна быть строка 0 0 0\n0 0 0, которая при выводе будет отображаться следующим образом:

0 0 0
0 0 0
Также экземпляр класса Matrix должен поддерживать унарные операторы +, - и ~:

результатом унарного + должен являться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с исходными элементами
результатом унарного - должен являться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с элементами, взятыми с противоположным знаком
результатом унарного ~ должен являться новый экземпляр класса Matrix, представляющий транспонированную матрицу
Наконец, при передаче экземпляра класса Matrix в функцию round() должен возвращаться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с элементами, округленными с помощью функции round(). Во время передачи в функцию round() должна быть возможность в качестве второго необязательного аргумента указать целое число, определяющее количество знаков после запятой при округлении.

Примечание 1. Индексация строк и столбцов в матрице начинается с нуля.
"""
import copy


class Matrix:

    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __repr__(self):
        return f'{self.__class__.__name__}{self.rows, self.cols}'
    def __str__(self):
        return '\n'.join(" ".join(map(str, row)) for row in self.matrix)

    def __pos__(self):
        new = Matrix(self.rows, self.cols, self.value)
        original = copy.deepcopy(self.matrix)
        new.matrix = original
        return new
    def __neg__(self):
        new = Matrix(self.rows, self.cols, self.value)
        original = copy.deepcopy(self.matrix)
        for i in range(len(original)):
            for j in range(len(original[i])):
                original[i][j] *= -1
        new.matrix = original
        return new

    def __invert__(self):
        new = Matrix(self.rows, self.cols, self.value)
        original = copy.deepcopy(self.matrix)
        inverted = [[0 for i in range(len(original))] for j in range(len(original[0]))]
        for i in range(len(original)):
            for j in range(len(original[0])):
                inverted[j][i] = original[i][j]
        new.matrix = inverted
        new.cols = self.rows
        new.rows = self.cols
        return new

    def __round__(self, n=None):
        new = Matrix(self.rows, self.cols, self.value)
        original = copy.deepcopy(self.matrix)
        for i in range(len(original)):
            for j in range(len(original[i])):
                original[i][j] = round(original[i][j], n)
        new.matrix = original
        return new
