"""
https://stepik.org/lesson/640040/step/23?unit=636560

Декоратор add_attrs
Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов и устанавливает их в качестве атрибутов декорируемой функции. Названием атрибута должно являться имя аргумента, значением атрибута — значение аргумента.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Вспомните про атрибут функции __dict__.
"""

from functools import wraps

def add_attrs(**kw):
    def decorator(func):
        for k, v in kw.items():
            func.__dict__[k] = v
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

