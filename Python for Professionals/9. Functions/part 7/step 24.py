"""
https://stepik.org/lesson/640039/step/24?auth=login&unit=636559

Декоратор takes_positive
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию, являются положительными целыми числами.

Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:

TypeError, если аргумент не является целым числом
ValueError, если аргумент является целым числом, но отрицательным или равным нулю
Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или при наличии разных аргументов, несоответствующих разным условиям: TypeError, затем ValueError.
"""

def takes_positive(func):
    def wrapper(*args, **kwargs):
        a = list(args) + list(kwargs.values())
        if not all(isinstance(i, int) for i in a):
            raise TypeError
        if not all(i>0 for i in a):
            raise ValueError
        return func(*args, **kwargs)
    return wrapper
