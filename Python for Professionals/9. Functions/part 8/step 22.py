"""
https://stepik.org/lesson/640040/step/22?unit=636560

Декоратор takes
Реализуйте декоратор takes, который принимает произвольное количество позиционных аргументов, каждый из которых является типом данных.

Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, принадлежат одному из этих типов. Если хотя бы один аргумент не принадлежит одному из данных типов, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

from functools import wraps

def takes(*a):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            z = args + tuple(kwargs.values())
            if not all(isinstance(j, a) for j in z):
                raise TypeError
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator
