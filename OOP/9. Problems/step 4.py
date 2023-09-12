"""
https://stepik.org/lesson/864077/step/4?unit=923013

Классы ArithmeticProgression и GeometricProgression
Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра класса ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:

progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10
Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.

Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии. При создании экземпляра класса GeometricProgression должны указываться первый член последовательности и знаменатель прогрессии:

progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8
Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной.
"""

class ArithmeticProgression:
    def __init__(self, start, step):
        self.start = start - step
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        return self.start

class GeometricProgression:

    def __init__(self, start, step):
        self.start = start / step
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= self.step
        return int(self.start)

