"""
https://stepik.org/lesson/669733/step/11?unit=667881

орождающий итераторы, конструктор которого принимает один аргумент:

number — ненулевое число
Итератор класса PowerOf должен генерировать бесконечную последовательность целых неотрицательных степеней числа number в порядке возрастания, начиная с нулевой степени.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимый класс PowerOf.
"""

class PowerOf:

    def __init__(self, number):
        self.number = number
        self.power = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.power += 1
        return self.number ** self.power

