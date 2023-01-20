"""
https://stepik.org/lesson/640044/step/22?unit=636564

Функция get_min_max() 😎
Реализуйте функцию get_min_max() c использованием функции enumerate(), которая принимает один аргумент:

data — список произвольных объектов, сравнимых между собой
Функция должна возвращать кортеж, в котором первым элементом является индекс минимального элемента в списке data, вторым — индекс максимального элемента в списке data. Если список data пуст, функция должна вернуть значение None.

Примечание 1. Если минимальных / максимальных элементов несколько, следует вернуть индексы первого по порядку элемента.
"""

def get_min_max(data):
    try:
        return data.index(min(data)), data.index(max(data))
    except:
        return

