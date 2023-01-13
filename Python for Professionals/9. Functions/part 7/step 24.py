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
        try:
            all(isinstance(i, int) for i in args)
            return func(*args, **kwargs)
        except TypeError as err:
            return type(err)
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))