"""
https://stepik.org/lesson/794484/step/18?unit=797232

Декоратор @recviz🌶️🌶️
Реализуйте декоратор @recviz, который полностью визуализирует выполнение декорируемой функции, в том числе и рекурсивной. Декоратор должен отображать все рекурсивные вызовы и возвращаемые значения, полученные при этих вызовах, причем рекурсивные вызовы, выполняемые в глубину, должны отделяться друг от друга четырьмя пробелами.

Очередной вызов декорируемой функции при визуализации должен включать в себя знак ->, имя декорируемой функции и аргументы, переданные при этом вызове. Возвращаемое значение при визуализации должно включать в себя знак <- и непосредственно само возвращаемое значение.

Примечание 1. Рекурсивный вызов и возвращаемое значение, полученное при этом вызове, должны находиться на одном уровне отступов.

Примечание 2. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""

from functools import wraps

def recwiz(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):