"""
https://stepik.org/lesson/651459/step/20?unit=648165

Функция sort_priority() 🌶️
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:

values — список чисел
group — список, кортеж или множество чисел
Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group, которая должна следовать первой.
"""

def sort_priority(values, group):
    return values.sort(key=lambda x: (x not in group, x))