"""
https://stepik.org/lesson/640040/step/21?unit=636560

Декоратор returns
Реализуйте декоратор returns, который принимает один аргумент:

datatype — тип данных
Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype. Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

from functools import wraps

def returns(datatype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            if isinstance(f, datatype):
                return f
            else:
                return TypeError
        return wrapper
    return decorator

