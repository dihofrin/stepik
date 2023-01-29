"""
https://stepik.org/lesson/668595/step/15?unit=666704

Функция is_iterator()
Реализуйте функцию is_iterator(), которая принимает один аргумент:

obj — произвольный объект
Функция должна возвращать True, если объект obj является итератором, или False в противном случае.
"""

def is_iterator(obj):
    return hasattr(obj, '__next__')
