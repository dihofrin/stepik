"""
https://stepik.org/lesson/805785/step/12?unit=816644

Класс CyclicList
Реализуйте класс CyclicList, описывающий циклический список. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов циклического списка. Если не передан, начальный набор элементов считается пустым
Класс CyclicList должен иметь два метода экземпляра:

append() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец циклического списка
pop() — метод, который принимает в качестве аргумента индекс элемента циклического списка, возвращает его значение и удаляет из циклического списка элемент с данным индексом. Если аргумент не передан, считается что имеется в виду последний элемент циклического списка
При передаче экземпляра класса CyclicList в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса CyclicList должен быть зацикленным итерируемым объектом. Другими словами, итерация по нему должна происходить бесконечно, и при каждом достижении его последнего элемента она должна начинаться сначала.

Наконец, экземпляр класса CyclicList должен позволять получать значения своих элементов с помощью индексов, при этом индексы должны работать циклически. Например, в циклическом списке [1, 2, 3] элементом с индексом 4 должно являться число 2.

Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.

Примечание 2. Экземпляр класса CyclicList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса CyclicList измениться  не должен.
"""

class CyclicList:

    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = -1

    def append(self, obj):
        return self.iterable.append(obj)

    def __getitem__(self, item):
        return self.iterable[item % len(self.iterable)]
    def pop(self, ind=-1):
        return self.iterable.pop(ind)

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.iterable[self.index % len(self.iterable)]


