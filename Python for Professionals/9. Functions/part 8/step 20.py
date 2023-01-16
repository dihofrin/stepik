"""
https://stepik.org/lesson/640040/step/20?unit=636560

Декоратор strip_range
Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:

start — неотрицательное целое число
end — неотрицательное целое число
char — одиночный символ, по умолчанию равный точке .
Декоратор должен изменять возвращаемое значение декорируемой функции, заменяя все символы в диапазоне индексов от start (включительно) до end (не включительно) на символ char.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.

Примечание 2. Гарантируется, что start < end.
"""

from functools import wraps

def strip_range(start, end, char='.'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            if end - start > len(f):
                f = f[:start] + char * (len(f) - len(f[:start]))
            else:
                f = f[:start] + (char * (end-start)) + f[end:]
            return f
        return wrapper
    return decorator
