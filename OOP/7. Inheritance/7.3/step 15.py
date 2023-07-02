"""
https://stepik.org/lesson/816515/step/15?unit=819845

Класс FuzzyString
Реализуйте класс FuzzyString, наследника класса str, описывающий строку, которая при любых сравнениях (==, !=, >, <, >=, <=) и проверках на принадлежность (in, not in) не учитывает регистр. Процесс создания экземпляра класса FuzzyString должен совпадать с процессом создания экземпляра класса str.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
"""

class FuzzyString(str):


    def __ne__(self, other):
        if isinstance(other, FuzzyString | str):
            return self.lower() != other.lower()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, FuzzyString | str):
            return self.lower() == other.lower()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, FuzzyString | str):
            return self.lower() > other.lower()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, FuzzyString | str):
            return self.lower() < other.lower()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, FuzzyString | str):
            return self.lower() >= other.lower()
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, FuzzyString | str):
            return self.lower() <= other.lower()
        return NotImplemented

    def __contains__(self, item):
        return item.lower() in self.lower()


