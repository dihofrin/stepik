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
                return func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(10, b=20))