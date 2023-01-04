"""
https://stepik.org/lesson/634520/step/20?unit=630783

Функция custom_sort() 🌶️
Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:

ordered_dict — словарь OrderedDict
by_values — булево значение, по умолчанию имеет значение False
Функция должна сортировать словарь ordered_dict:

по ключам, если by_values имеет значение False
по значениям, если by_values имеет значение True
Примечание 1. Функция должна изменять переданный словарь, а не возвращать новый. Возвращаемым значением функции должно быть None.

Примечание 2. Гарантируется, что переданный в функцию словарь можно отсортировать, то есть он не содержит ключи, имеющие разные типы, а также значения, имеющие разные типы.

Примечание 3. Если два элемента имеют равные значения, то следует сохранить их исходный порядок следования.

Примечание 4. Files. В тестирующую систему сдайте программу, содержащую только необходимую функцию custom_sort(), но не код, вызывающий ее.
"""

from collections import OrderedDict

def custom_sort(ordered_dict, by_values = False):
    if by_values:
        dict = OrderedDict(sorted(ordered_dict.items(), key=lambda item: item[1]))
    else:
        dict = OrderedDict(sorted(ordered_dict.items()))
    for key in dict:
        ordered_dict.move_to_end(key)
    return None