"""
https://stepik.org/lesson/794698/step/15?unit=797450

Класс StrExtension
Реализуйте класс StrExtension, описывающий набор функций для работы со строками. При создании экземпляра класс не должен принимать никаких аргументов.

Класс StrExtension должен иметь три статических метода:

remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные латинские буквы без учета регистра и возвращает полученный результат
leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы, не являющиеся латинскими буквами, и возвращает полученный результат
replace_all() — метод, который принимает три строковых аргумента string, chars и char, заменяет в строке string все символы из chars на char с учетом регистра и возвращает полученный результат.
Примечание 1. Гарантируется, что все буквенные символы относятся к латинскому алфавиту.

Примечание 2. Латинские гласные буквы: a, e, i, o, u, y.
"""

from string import ascii_lowercase

class StrExtension:

    def __init__(self,):
        pass

    @staticmethod
    def remove_vowels(s):
        return ''.join(i for i in s if i.lower() not in 'aeiouy')

    @staticmethod
    def leave_alpha(s):
        return ''.join(i for i in s if i.lower() in ascii_lowercase)

    @staticmethod
    def replace_all(s, chars, char):
        r = ''
        for i in s:
            if i in chars:
                r += char
            else:
                r += i
        return r

print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))