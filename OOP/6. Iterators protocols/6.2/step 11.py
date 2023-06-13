"""
https://stepik.org/lesson/805785/step/11?unit=816644

Класс SparseArray
Разреженный массив (список) — абстрактное представление обычного массива (списка), в котором данные представлены не непрерывно, а фрагментарно: большинство его элементов принимает одно и то же значение по умолчанию, обычно 0 или None. В разреженном массиве возможен доступ к неопределенным элементам, в этом случае массив вернет некоторое значение по умолчанию.

Реализуйте класс SparseArray, описывающий разреженный массив. При создании экземпляра класс должен принимать один аргумент:

default — значение по умолчанию для неопределенных элементов разреженного массива
Экземпляр класса SparseArray должен позволять получать и изменять значения своих элементов с помощью индексов. При попытке получить значение элемента по несуществующему индексу должно быть возвращено значение по умолчанию.
"""

class SparseArray:

    def __init__(self, default):
        self.default = default
        self.array = [default]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Index must be integer')
        if key >= len(self.array):
            self.array = self.array + [self.default for _ in range(key+1)]
        self.array[key] = value

    def __getitem__(self, item):
        return self.array[item]


