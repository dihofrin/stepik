"""
https://stepik.org/lesson/805785/step/13?unit=816644

Класс SequenceZip
Реализуйте класс SequenceZip. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является итерируемым объектом. Класс SequenceZip должен описывать последовательность, элементами которой являются элементы переданных в конструктор итерируемых объектов, объединенные в кортежи. Объединение должно происходить аналогично тому, как это делает функция zip().

При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса SequenceZip должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Экземпляр класса SequenceZip не должен зависеть от итерируемых объектов, на основе которых он был создан. Другими словами, если исходные итерируемые объекты изменятся, то экземпляр класса SequenceZip измениться  не должен.
"""

from copy import deepcopy

class SequenceZip:

    def __init__(self, *args):
        self.args = zip(*args)
        self.index = -1

    def __len__(self):
        yield len(deepcopy(tuple(self.args)))

    def __iter__(self):
        yield from deepcopy(self.args)

    def __next__(self):
        s = deepcopy(self.args)
        self.index += 1
        if self.index >= len(s):
            raise StopIteration
        return s[self.index]

    def __getitem__(self, item):
        return tuple(self.args)[item]

many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])