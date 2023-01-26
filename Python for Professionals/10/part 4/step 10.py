"""
https://stepik.org/lesson/669733/step/10?unit=667881

Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.

Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 1
"""

class Fibonacci:

    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.second
        self.second += self.first
        self.first = result
        return result

