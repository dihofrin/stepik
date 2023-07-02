"""
https://stepik.org/lesson/816515/step/13?unit=819845

Класс UpperPrintString
Реализуйте класс UpperPrintString, наследника класса str, описывающий строку. Процесс создания экземпляра класса UpperPrintString должен совпадать с процессом создания экземпляра класса str.

Экземпляр класса UpperPrintString должен иметь следующее неформальное строковое представление:

<значение строки в верхнем регистре>
"""

class UpperPrintString(str):

    def __str__(self):
        return f'{self.upper()}'
