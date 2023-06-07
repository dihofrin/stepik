"""
https://stepik.org/lesson/805786/step/18?unit=816645

Класс SkipIterator
Реализуйте класс SkipIterator. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

iterable — итерируемый объект
n — целое неотрицательное число
Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable, пропуская по n элементов, а затем возбуждает исключение StopIteration.
"""

class SkipIterator:

    def __init__(self, iterable, n):
        self.iterable = list(iterable)
        self.n = n+1
        self.index = -1-n

    def __iter__(self):
        return self

    def __next__(self):
        self.index += self.n
        if self.index >= len(self.iterable):
            raise StopIteration
        return self.iterable[self.index]
