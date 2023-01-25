"""
https://stepik.org/lesson/669733/step/9?unit=667881

Итератор Square
Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:

n — натуральное число,
Итератор класса Square должен генерировать последовательность из n чисел, каждое из которых является квадратом очередного натурального числа, а затем возбуждать исключение StopIteration.

Примечание 1. Последовательность квадратов натуральных чисел начинается с квадрата числа
1
1.
"""

class Square:

    def __init__(self, n):
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index <= self.n:
            return self.index ** 2
        else:
            raise StopIteration


squares = Square(2)

print(next(squares))
print(next(squares))