"""
https://stepik.org/lesson/933767/step/9?unit=939666

Класс Reloopable
Реализуйте класс Reloopable. При создании экземпляра класс должен принимать один аргумент:

file — открытый на чтение файловый объект
Экземпляр класса Reloopable должен являться контекстным менеджером, который позволяет многократно итерироваться по файловому объекту file внутри блока with. Также контекстный менеджер должен закрывать используемый им файловый объект после выполнения кода внутри блока with.
"""

class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.lines = self.file.readlines()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

