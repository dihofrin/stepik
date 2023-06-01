"""
https://stepik.org/lesson/805787/step/17?unit=808914

Декоратор @CachedFunction
Реализуйте декоратор @CachedFunction, который кэширует вычисленные значения декорируемой функции. Кэш должен быть доступен по атрибуту cache и представлять собой словарь, ключом в котором является кортеж с аргументами, а значением — возвращаемое значение декорируемой функции при вызове с этими аргументами.

Примечание 1. Для однозначного кеширования гарантируется, что декорируемая функция принимает только позиционные аргументы.
"""

class CachedFunction:

    cache = dict()

    def __init__(self,func):
        self.func = func

    def __call__(self, *args):
        key = args
        result = self.cache.get(key)
        if result is None:
            result = self.func(*args)
            self.cache[key] = result
        return result
