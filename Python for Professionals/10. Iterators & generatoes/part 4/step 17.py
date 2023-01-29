"""
https://stepik.org/lesson/669733/step/17?unit=667881

Итератор Xrange 🌶️
Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:

start — целое или вещественное число
end — целое или вещественное число
step — целое или вещественное число, по умолчанию имеет значение
1
1
Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end, включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration.
"""

class Xrange:

    def __init__(self, start, end, step=1):
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step < 0 and self.start + self.step <= self.end or self.step > 0 and self.start + self.step >= self.end:
                raise StopIteration
        self.start += self.step
        return self.start
