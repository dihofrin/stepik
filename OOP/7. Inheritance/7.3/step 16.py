"""
https://stepik.org/lesson/816515/step/16?unit=819845

Класс TitledText
Реализуйте класс TitledText, наследника класса str, который описывает текст, имеющий заголовок. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

content — текст
text_title — заголовок текста
Класс TitleText должен иметь один метод экземпляра:

title() — метод, возвращающий заголовок текста
Примечание 1. Значением экземпляра класса TitledText должен быть именно текст, а не заголовок текста или текст вместе с заголовком.
"""

class TitledText(str):

    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance


    def title(self):
        return self.text_title

