"""
https://stepik.org/lesson/640040/step/19?unit=636560

Декоратор repeat
Реализуйте декоратор repeat, который принимает один аргумент:

times — натуральное число
Декоратор должен вызывать декорируемую функцию times раз.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

from functools import wraps

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                f = func(*args, **kwargs)
            return f
        return wrapper
    return decorator
