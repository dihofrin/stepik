"""
https://stepik.org/lesson/655394/step/16?unit=652334

Функция cyclic_shift()
Реализуйте функцию cyclic_shift() с использованием аннотаций типов, которая принимает два аргумента в следующем порядке:

numbers — список целых или вещественных чисел
step — целое число
Функция должна изменять переданный список, циклически сдвигая элементы списка на step шагов, и возвращать значение None. Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.
"""

def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step < 0:
        step %= len(numbers)
    for i in range(step):
        numbers.insert(0, numbers.pop())