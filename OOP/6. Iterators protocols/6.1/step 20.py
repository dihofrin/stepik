"""
https://stepik.org/lesson/805786/step/20?unit=816645

Класс Peekable 🌶️
Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.

Класс Peekable должен иметь один метод экземпляра:

peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий итератор. Если итератор пуст, должно быть возбуждено исключение StopIteration. Также метод должен уметь принимать один необязательный аргумент default — объект, который будет возвращен вместо возбуждения исключения StopIteration, если итератор пуст
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс Peekable должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.
"""

class Peekable:

    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterable:
            return self.iterable.pop(0)
        raise StopIteration

    def peek(self, default=StopIteration):
        while self.iterable:
            return self.iterable[0]
        if not self.iterable:
            if isinstance(default, Exception):
                return default
            else:
                raise default

from itertools import islice

iterator = Peekable([1, 2, 3])

print(iterator.peek())
print(list(islice(iterator, 2)))
print(iterator.peek())
print(list(iterator))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')