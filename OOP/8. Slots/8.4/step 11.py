"""
https://stepik.org/lesson/808351/step/11?auth=login&unit=811596

Декоратор @limited_calls
Реализуйте класс декоратор @limited_calls, который принимает один аргумент:

n — целое число
Декоратор должен разрешать вызывать декорируемую функцию n раз. Если декорируемая функция вызывается более n раз, должно быть возбуждено исключение MaxCallsException с текстом:

Превышено допустимое количество вызовов
"""

class MaxCallsException(Exception):
    pass

from functools import wraps

class limited_calls:
    def __init__(self, n):
        self.n = n
        self.calls = 0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.calls < self.n:
                value = func(*args, **kwargs)
                self.calls += 1
                return value
            raise MaxCallsException('Превышено допустимое количество вызовов')
        return wrapper

@limited_calls(3)
def add(a, b):
    return a + b

print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)