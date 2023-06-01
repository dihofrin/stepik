"""
https://stepik.org/lesson/794698/step/16?unit=797450

Класс CaseHelper 🌶️
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case. При создании экземпляра класс не должен принимать никаких аргументов.

Класс CaseHelper должен иметь четыре статических метода:

is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Snake Case, или False в противном случае
is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Upper Camel Case, или False в противном случае
to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в стиле Snake Case и возвращает полученный результат
to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, записывает ее в стиле Upper Camel Case и возвращает полученный результат
"""

class CaseHelper:

    @staticmethod
    def is_snake(s):
        return all(i.isalpha() and i.islower() for i in s.split('_'))

    @staticmethod
    def is_upper_camel(s):
        return all(i.isalpha() for i in s) and s[0].istitle()

    @staticmethod
    def to_snake(s):
        snake_case = ''
        for char in s:
            if char.isupper():
                if snake_case:
                    snake_case += '_'
                snake_case += char.lower()
            else:
                snake_case += char
        return snake_case

    @staticmethod
    def to_upper_camel(s):
        return ''.join(i.title() for i in s.split('_'))
