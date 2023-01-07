"""
https://stepik.org/lesson/647292/step/12?unit=643926

Новый print()
Напишите программу, которая переопределяет встроенную функцию print() так, чтобы она печатала все переданные строковые аргументы в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.
"""

old_print = print

def my_func(*args, sep=' ', end='\n'):
    s = []
    for i in args:
        if isinstance(i, str):
            s.append(i.upper())
        else:
            s.append(i)
    old_print(*s, sep=sep.upper(), end=end.upper())

print = my_func
