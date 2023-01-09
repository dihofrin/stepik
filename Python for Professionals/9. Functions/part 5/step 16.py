"""
https://stepik.org/lesson/651459/step/16?unit=648165

Функция power()
Реализуйте функцию power(), которая принимает один аргумент:

degree — целое число
Функция power() должна возвращать функцию, которая принимает в качестве аргумента целое число x и возвращает значение x в степени degree.
"""

def power(degree):
    return lambda x: x ** degree