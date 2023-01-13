"""
https://stepik.org/lesson/640039/step/21?auth=login&unit=636559

Декоратор do_twice
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.
"""

def do_twice(func):
    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper