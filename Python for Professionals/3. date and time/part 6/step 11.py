"""
https://stepik.org/lesson/570055/step/11?unit=564599

Функция get_the_fastest_func()
Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:

funcs — список произвольных функций
arg — произвольный объект
Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.

Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_the_fastest_func(), но не код, вызывающий ее.
"""

import time

def get_the_fastest_func(funcs, arg):
    result = 0
    max = 100000000000000000
    tmp = 0
    def measure(foo, bar):
        start = time.perf_counter()
        foo(bar)
        return time.perf_counter()-start
    for i in funcs:
        tmp = measure(i, arg)
        if tmp < max:
            max = tmp
            result = i
    return result