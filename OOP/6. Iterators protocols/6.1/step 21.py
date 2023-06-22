"""
https://stepik.org/lesson/805786/step/21?unit=816645

Класс LoopTracker🌶️🌶️
Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.

Класс LoopTracker должен иметь четыре свойства:

accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором на данный момент
empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент опустевшего итератора
first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его. Если итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта, то должно быть возбуждено исключение AttributeError с текстом:
Исходный итерируемый объект пуст
last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный момент. Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError с текстом:
Последнего элемента нет
Класс LoopTracker должен иметь один метод экземпляра:

is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае
"""

class LoopTracker:

    def __init__(self, iterable):
        self.iterable = iterable
        self.count = -1
        self._first = self.iterable[0]
        self._last = self.iterable[-1]
        self._empty_accesses = 0

    @property
    def accesses(self):
        return self.count + 1

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if not self.iterable:
            raise AttributeError('Исходный итерируемый объект пуст')
        return self._first

    @property
    def last(self):
        return self._last

    def is_empty(self):
        return self.count < len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count >= len(self.iterable):
            self._empty_accesses += 1
            raise StopIteration
        if self.count == 0:
            self._first = self.iterable[self.count]
        self._last = self.iterable[self.count]
        return self.iterable[self.count]


loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())