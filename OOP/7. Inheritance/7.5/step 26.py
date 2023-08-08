"""
https://stepik.org/lesson/872533/step/26?unit=876917

Класс SortedList
Реализуйте класс SortedList, описывающий список, который автоматически сортируется при создании и любом изменении. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов отсортированного списка. Если не передан, начальный набор элементов считается пустым
Класс SortedList должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в экземпляр класса SortedList
discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий все его включения из экземпляра класса SortedList, если он в нем присутствует
update() — метод, принимающий в качестве аргумента итерируемый объект и добавляющий все его элементы в экземпляр класса SortedList
Также класс SortedList должен иметь такие методы экземпляра, как append(), insert(), extend() и reverse(), при попытке воспользоваться которыми должно быть возбуждено исключение NotImplementedError.

Экземпляр класса SortedList должен иметь следующее формальное строковое представление:

SortedList([<первый элемент списка>, <второй элемент списка>, ...])
При передаче экземпляра класса SortedList в функцию len() должно возвращаться количество элементов в нем. При попытке передачи экземпляра класса SortedList в функцию reversed() должно быть возбуждено исключение NotImplementedError.

Помимо этого, экземпляр класса SortedList должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Также экземпляр класса SortedList должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Вдобавок ко всему, экземпляр класса SortedList должен позволять получать и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. При попытке изменить значение элемента по его индексу должно быть возбуждено исключение NotImplementedError.

Экземпляры класса SortedList должны поддерживать между собой арифметические операции с помощью операторов + и +=:

оператор + должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться новый экземпляр класса SortedList
оператор += должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться левый экземпляр класса SortedList
Наконец, экземпляр класса SortedList должен поддерживать операцию умножения на целое число n с помощью операторов * и *=:

оператор * должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться новый экземпляр класса SortedList
оператор *= должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться левый экземпляр класса SortedList
Примечание 1. Гарантируется, что элементами одного экземпляра класса SortedList являются объекты, сравнимые между собой.
"""

from collections.abc import MutableSequence

class SortedList(MutableSequence):


    def __init__(self, iterable=()):
        self.iterable = sorted(list(iterable))


    def add(self, other):
        if isinstance(other, list | SortedList):
            self.iterable.extend(other)
        else:
            self.iterable.append(other)
        self.iterable = sorted(self.iterable)
    def discard(self, obj):
        self.iterable = sorted([item for item in self.iterable if item != obj])


    def update(self, iterable):
        self.iterable.extend(iterable)
        self.iterable = sorted(self.iterable)

    def __repr__(self):
        return f'SortedList({self.iterable})'

    def __len__(self):
        return len(self.iterable)

    def __reversed__(self):
        raise NotImplementedError

    def __contains__(self, item):
        return item in self.iterable

    def __getitem__(self, item):
        if isinstance(item, int | slice):
            return self.iterable[item]
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        del self.iterable[key]

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self.iterable + other.iterable)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            self.iterable += other.iterable
            self.iterable.sort()
            return self
        return NotImplemented


    def __mul__(self, other):
        if isinstance(other, int):
            return SortedList(self.iterable * other)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.iterable = sorted(self.iterable * other)
            return self
        return NotImplemented

    @staticmethod
    def _not_implemented_error(*args, **kwargs):
        raise NotImplementedError

    append = insert = extend = reverse = _not_implemented_error
