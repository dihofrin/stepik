"""
https://stepik.org/lesson/808351/step/14?auth=login&unit=811596

Декоратор @exception_decorator
Реализуйте класс декоратор @exception_decorator, который возвращает

кортеж (value, None), если декорируемая функция завершила свою работу без возбуждения исключения, где value — возвращаемое значение декорируемой функции
кортеж (None, errortype), если во время выполнения декорируемой функции было возбуждено исключение, где errortype — тип возбужденного исключения
"""

from functools import update_wrapper

class exception_decorator:

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            value = self.func(*args, **kwargs)
            return value, None
        except Exception as e:
            return None, type(e)

