"""
https://stepik.org/lesson/933767/step/16?unit=939666

Класс AdvancedTimer
Реализуйте класс AdvancedTimer. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса AdvancedTimer должен являться многоразовым контекстным менеджером, который замеряет время выполнение кода внутри каждого блока with.

Также экземпляр класса AdvancedTimer должен иметь четыре атрибута:

last_run — число, представляющее время выполнения кода внутри последнего блока with
runs — список чисел, каждое из которых представляет время выполнения какого-либо кода внутри блока with. Первый элемент списка должен представлять собой время выполнения кода внутри первого блока with, второй элемент — внутри второго блока with, и так далее
min — число, представляющее минимальное время выполнения кода внутри блока with среди всех замеров
max — число, представляющее максимальное время выполнения кода внутри блока with среди всех замеров
Если экземпляр класса AdvancedTimer ни разу не использовался для замера скорости выполнения какого-либо блока кода, значения атрибутов last_run, min и max должны равняться None.
"""

from time import perf_counter
class AdvancedTimer:

    def __init__(self):
        self.last_run = self.min = self.max = None
        self.runs = []

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.last_run = perf_counter() - self.start
        self.runs.append(self.last_run)
        self.min = min(self.runs)
        self.max = max(self.runs)

