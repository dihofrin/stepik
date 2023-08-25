"""
https://stepik.org/lesson/808351/step/10?unit=811596

Декоратор @reverse_args
Вам доступен декоратор @reverse_args, который передает все позиционные аргументы в декорируемую функцию в обратном порядке. Реализуйте декоратор @reverse_args в виде класса декоратора.
"""


from functools import update_wrapper
class reverse_args:

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*reverse_args(args), **kwargs)

