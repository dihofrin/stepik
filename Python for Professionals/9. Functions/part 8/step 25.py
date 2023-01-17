"""
https://stepik.org/lesson/640040/step/25?unit=636560


Декоратор retry
Реализуйте декоратор retry, который принимает один аргумент:

times — натуральное число
Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время ее выполнения возникает ошибка. Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times, после чего должен возбуждать исключение MaxRetriesException.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

from functools import wraps


class MaxRetriesException(Exception):
    pass
def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException
        return wrapper
    return decorator
