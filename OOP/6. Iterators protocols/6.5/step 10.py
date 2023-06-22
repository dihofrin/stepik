"""
https://stepik.org/lesson/933767/step/10?unit=939666

Класс UpperPrint
Реализуйте класс UpperPrint. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса UpperPrint должен являться контекстным менеджером, который внутри блока with позволяет выполнять все операции записи в стандартный поток вывода sys.stdout в верхнем регистре.
"""
import sys


class UpperPrint:

    def __enter__(self):
        self.standart_output = sys.stdout.write
        upper = lambda text: self.standart_output(text.upper())
        sys.stdout.write = upper

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.standart_output
