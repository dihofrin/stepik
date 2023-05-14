"""
https://stepik.org/lesson/794582/step/12?unit=797335

Класс TextHandler
Будем называть словом любую последовательность из одной или более букв. Текстом будем считать набор слов, разделенных пробелами.

Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса TextHandler должен иметь три метода:

add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста в набор
get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе
Примечание 1. Слова в списках, возвращаемых методами get_shortest_words() и get_longest_words(), должны располагаться в том порядке, в котором они были добавлены в набор.
"""

class TextHandler:

    def __init__(self):
        self.l = list()

    def add_words(self, text):
        self.l += text.split()
        self.srt = sorted(self.l, key=len)
        return self.l

    def get_shortest_words(self):
        return [i for i in self.l if len(i) == len(self.srt[0])]

    def get_longest_words(self):
        return [i for i in self.l if len(i) == len(self.srt[-1])]
