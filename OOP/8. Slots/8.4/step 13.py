"""
https://stepik.org/lesson/808351/step/13?auth=login&unit=811596

Декоратор @returns
Реализуйте класс декоратор @returns, который принимает один аргумент:

datatype — тип данных
Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype. Если возвращаемое значение принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError.
"""

from functools import wraps

class returns:

    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if isinstance(value, self.datatype):
                return value
            raise TypeError
        return wrapper
