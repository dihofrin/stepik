"""
https://stepik.org/lesson/816515/step/19?unit=819845


Класс AdvancedTuple
Реализуйте класс AdvancedTuple, наследника класса tuple, который описывает кортеж, умеющий выполнять операцию сложения (+, +=) не только с экземплярами классов AdvancedTuple и tuple, но и с любыми итерируемыми объектами. Процесс создания экземпляра класса AdvancedTuple должен совпадать с процессом создания экземпляра класса tuple.

Примечание 1. Как бы ни выполнялось сложение, с помощью оператора + или +=, результатом операции должен являться новый экземпляр класса AdvancedTuple.
"""

class AdvancedTuple(tuple):

    def __add__(self, other):
        return AdvancedTuple(tuple(self) + tuple(other))

    def __radd__(self, other):
        return AdvancedTuple(tuple(other) + tuple(self))

