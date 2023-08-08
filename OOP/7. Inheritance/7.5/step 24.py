"""
https://stepik.org/lesson/872533/step/24?unit=876917

Класс BitArray
Реализуйте класс BitArray, описывающий битовый список, то есть список, элементами которого являются только нули и единицы. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов битового списка. Если не передан, начальный набор считается пустым
Экземпляр класса BitArray должен иметь следующее неформальное строковое представление:

[<первый элемент битового списка>, <второй элемент битового списка>, ...]
При передаче экземпляра класса BitArray в функцию len() должно возвращаться количество элементов в нем. При передаче экземпляра класса BitArray в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса BitArray , расположенные в обратном порядке.

Экземпляр класса BitArray должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Помимо этого, экземпляр класса BitArray должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Также экземпляр класса BitArray должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.

Вдобавок ко всему, экземпляр класса BitArray должен поддерживать унарный оператор ~, выполняющий операцию логического отрицания для каждого бита битового списка, тем самым преобразуя 0 в 1, а 1 в 0. Результатом работы оператора должен являться новый экземпляр класса BitArray.

Наконец, экземпляры класса BitArray должны поддерживать между собой логические операции с помощью операторов & и |:

оператор & должен выполнять операцию логического И над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray

оператор | должен выполнять операцию логического ИЛИ над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray

Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.
"""

from collections.abc import Sequence

class BitArray(Sequence):

    def __init__(self, iterable=()):
        self.iterable = list(iterable)

    def __repr__(self):
        return f'{self.iterable}'

    def __contains__(self, item):
        return item in self.iterable

    def __getitem__(self, item):
        if isinstance(item, int | slice):
            return self.iterable[item]
        return NotImplemented

    def __len__(self):
        return len(self.iterable)

    def __invert__(self):
        return BitArray(int(not item) for item in self.iterable)

    def __and__(self, other):
        if isinstance(other, BitArray):
            return BitArray(self_item and other_item for self_item, other_item in zip(self.iterable, other.iterable))
        return NotImplemented

    def __or__(self, other):
        if isinstance(other, BitArray):
            return BitArray(self_item or other_item for self_item, other_item in zip(self.iterable, other.iterable))
        return NotImplemented
