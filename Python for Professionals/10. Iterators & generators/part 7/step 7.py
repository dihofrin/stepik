"""
https://stepik.org/lesson/673155/step/7?unit=671418


Функция filter_names()
Реализуйте генераторную функцию filter_names(), которая принимает три аргумента в следующем порядке:

names — список имен
ignore_char — одиночный символ
max_names — натуральное число
Функция должна возвращать генератор, порождающий max_names имён из списка names, игнорируя имена, которые

начинаются на ignore_char (в любом регистре)
содержат хотя бы одну цифру
Если max_names больше количества имен в списке names, то генератор должен породить все возможные имена из данного списка.

Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в своем исходном порядке.
"""

def filter_names(names, ignore_char, max_names):
    names1 = (name for name in names if name[0].lower() != ignore_char.lower() and not any(map(str.isdigit, name)))
    for _ in range(max_names):
        try:
            yield next(names1)
        except:
            return

