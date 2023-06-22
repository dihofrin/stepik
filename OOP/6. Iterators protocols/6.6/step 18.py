"""
https://stepik.org/lesson/934146/step/18?unit=940038

Контекстный менеджер reversed_print
Реализуйте контекстный менеджер reversed_print с помощью декоратора @contextmanager, который не принимает никаких аргументов.

Контекстный менеджер reversed_print должен позволять выполнять все операции записи в стандартный поток вывода sys.stdout внутри блока with в обратном порядке..
"""
import sys
from contextlib import contextmanager
@contextmanager
def reversed_print():
    old_write = sys.stdout.write
    sys.stdout.write = lambda text: old_write(text[::-1])
    yield
    sys.stdout.write = old_write


with reversed_print():
    print('python')
    print('beegeek')

print('Вывод вне блока with')