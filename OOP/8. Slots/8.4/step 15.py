"""
https://stepik.org/lesson/808351/step/15?auth=login&unit=811596

Декоратор @ignore_exception
Реализуйте класс декоратор @ignore_exception, который принимает произвольное количество позиционных аргументов — типов исключений, и выводит текст:

Исключение <тип исключения> обработано
если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов. Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.
"""

from functools import wraps

class ignore_exception:

    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except self.args as e:
                print(f'Исключение {type(e).__name__} обработано')
        return wrapper
