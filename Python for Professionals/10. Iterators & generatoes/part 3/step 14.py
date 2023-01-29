"""
https://stepik.org/lesson/668595/step/14?unit=666704

Функция is_iterable()
Реализуйте функцию is_iterable(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, или False в противном случае.
"""

def is_iterable(obj):
    return hasattr(obj, '__iter__')
