"""
https://stepik.org/lesson/805771/step/18?unit=808896

Класс Word
Будем называть словом любую последовательность из одной или более латинских букв.

Реализуйте класс Word, описывающий слово. При создании экземпляра класс должен принимать один аргумент:

word — слово
Экземпляр класса Word должен иметь следующее формальное строковое представление:

Word('<слово в исходном виде>')
И следующее неформальное строковое представление:

<слово, в котором первая буква заглавная, а все остальные строчные>
Также экземпляры класса Word должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два слова считаются равными, если их длины совпадают. Слово считается больше другого слова, если его длина больше.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
"""

from functools import total_ordering

@total_ordering
class Word:

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.word)})'

    def __str__(self):
        return self.word.title()
    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented
