"""
https://stepik.org/lesson/805787/step/11?unit=808914

Класс Dice
Реализуйте класс Dice, описывающий игральный кубик с определенным количеством граней. При создании экземпляра класс должен принимать один аргумент:

sides — количество граней игрального кубика
Экземпляр класса Dice должен являться вызываемым объектом и не принимать никаких аргументов. При вызове он должен возвращать значение случайной грани игрального кубика. Например, если кубик имеет 6 граней, экземпляр класса Dice должен вернуть случайное число из диапазона [1; 6].
"""

from random import randint

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return randint(1, self.sides)

kingdice = Dice(6)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [7, 8, 9, 10])


def pizda(s=1,k=1, v=None):
    print(dir())
    return v

pizda()