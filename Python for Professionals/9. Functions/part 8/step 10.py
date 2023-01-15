"""
https://stepik.org/lesson/640040/step/10?unit=636560

Декоратор returns_string
Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение декорируемой функции принадлежит типу str. Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

from functools import wraps

def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not isinstance(func(*args, **kwargs), str):
            raise TypeError
        return func(*args, **kwargs)
    return wrapper