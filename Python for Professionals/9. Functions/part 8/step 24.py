"""
https://stepik.org/lesson/640040/step/24?unit=636560

Декоратор ignore_exception
Реализуйте декоратор ignore_exception, который принимает произвольное количество позиционных аргументов — типов исключений, и выводит текст:

Исключение <тип исключения> обработано
если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.

Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

from functools import wraps

def ignore_exception(*a):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                if type(err) in a:
                    print(f'Исключение {type(err).__name__} обработано')
                else:
                    raise err
        return wrapper
    return decorator