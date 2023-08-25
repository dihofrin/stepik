"""
https://stepik.org/lesson/808351/step/12?auth=login&unit=811596

Декоратор @takes_numbers
Реализуйте класс декоратор @takes_numbers, который проверяет, что все аргументы, передаваемые в декорируемую функцию, принадлежат типам int или float. Если хотя бы один аргумент принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:

Аргументы должны принадлежать типам int или float
"""

from functools import update_wrapper

class takes_numbers:

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        if all(isinstance(arg, (int, float)) for arg in args + tuple(kwargs.values())):
            return self.func(*args, **kwargs)
        raise TypeError('Аргументы должны принадлежать типам int или float')