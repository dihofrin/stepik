"""
https://stepik.org/lesson/640040/step/9?unit=636560

Декоратор square
Реализуйте декоратор square, который возводит возвращаемое значение декорируемой функции во вторую степень.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа int или float.
"""

from functools import wraps

def square(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

@square
def add(a, b):
    '''прекрасная функция'''
    return a + b

print(add(1, 1))
print(add.__name__)
print(add.__doc__)