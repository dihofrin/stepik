"""
https://stepik.org/lesson/666563/step/17?unit=664567

<<<<<<< HEAD
=======
Функция first_largest()
>>>>>>> 87afb17 (section 10.10)
Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект, элементами которого являются целые числа
number — произвольное число
<<<<<<< HEAD
Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который больше number. Если таких элементов нет, функция должна вернуть число −1.
"""
=======
Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который больше number. Если таких элементов нет, функция должна вернуть число  -1.
"""

>>>>>>> 87afb17 (section 10.10)
from itertools import dropwhile
def first_largest(iterable, number):
    for index in dropwhile(lambda x: x[1] < number, enumerate(iterable)):
        return index[0]
    return -1
