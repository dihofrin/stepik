"""
https://stepik.org/lesson/640039/step/22?auth=login&unit=636559

Декоратор reverse_args
Реализуйте декоратор reverse_args, который передает все позиционные аргументы в декорируемую функцию func в обратном порядке.
"""

def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper