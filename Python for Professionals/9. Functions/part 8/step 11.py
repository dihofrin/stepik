"""
https://stepik.org/lesson/640040/step/11?unit=636560

Декоратор trace
Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения, а именно: имя функции, переданные аргументы и возвращаемое значение в следующем формате:

TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(func(*args, **kwargs))}')
        return func(*args, **kwargs)
    return wrapper