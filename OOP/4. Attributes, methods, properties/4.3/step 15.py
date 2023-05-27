"""
https://stepik.org/lesson/794582/step/15?unit=797335

Класс Wordplay
Будем называть словом любую последовательность из одной или более латинских букв.

Реализуйте класс Wordplay, описывающий расширяемый набор слов. При создании экземпляра класс должен принимать один аргумент:

words — список, определяющий начальный набор слов. Если не передан, начальный набор слов считается пустым
Экземпляр класса Wordplay должен иметь один атрибут:

words — список, содержащий набор слов
Класс Wordplay должен иметь четыре метода экземпляра:

add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор. Если слово уже есть в наборе, метод ничего не должен делать
words_with_length() — метод, принимающий в качестве аргумента натуральное число n и возвращающий список слов из набора, длина которых равна n
only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из набора, которые состоят только из переданных букв
avoid() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из списка words, которые не содержат ни одну из этих букв
Примечание 1. Слова в списках, возвращаемых методами words_with_length(), only() и avoid(), должны располагаться в том порядке, в котором они были добавлены.

Примечание 2. Экземпляр класса Wordplay не должен зависеть от списка, на основе которого он был создан. Другими словами, если исходный список изменится, то экземпляр класса Wordplay измениться не должен.
"""

class Wordplay:

    def __init__(self, words=None):
        if not words:
            self.words = list()
        else:
            self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        if self.words:
            return [i for i in self.words if len(i) == n]
        return list()

    def only(self, *args):
        if self.words:
            return [i for i in self.words if set(i).issubset(set(args))]
        return list()

    def avoid(self, *args):
        if self.words:
            return [i for i in self.words if not set(args) & set(i)]
        return list()