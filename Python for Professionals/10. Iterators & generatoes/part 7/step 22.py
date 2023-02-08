"""
https://stepik.org/lesson/673155/step/22?unit=671418

Функция pairwise()
Реализуйте генераторную функцию, которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых содержит очередной элемент итерируемого объекта iterable, а также следующий за ним элемент:

(<очередной элемент>, <следующий элемент>)
Для последнего элемента следующим считается значение None.
"""

def pairwise(iterable):
    if iterable:
        it = iter(iterable)
        first = next(it, None)
        second = next(it, None)
        while True:
            yield first, second
            first = second
            if first is None:
                return
            second = next(it, None)

