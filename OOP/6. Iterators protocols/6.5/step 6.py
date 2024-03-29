"""
https://stepik.org/lesson/933767/step/6?unit=939666

Класс Greeter
Реализуйте класс Greeter. При создании экземпляра класс должен принимать один аргумент:

name — имя пользователя
Экземпляр класса Greeter должен иметь один атрибут:

name — имя пользователя
Экземпляр класса Greeter должен являться контекстным менеджером, который приветствует пользователя с именем name перед выполнением блока with и выводит текст:

Приветствую, <имя пользователя>!
а также прощается с ним после выполнения блока with и выводит текст:

До встречи, <имя пользователя>!
"""

class Greeter:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'До встречи, {self.name}!')