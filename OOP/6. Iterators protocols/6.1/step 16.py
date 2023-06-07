"""
https://stepik.org/lesson/805786/step/16?unit=816645

Класс DevelopmentTeam
Реализуйте класс DevelopmentTeam, описывающий команду разработчиков двух уровней: junior (младший) и senior (старший). При создании экземпляра класс не должен принимать никаких аргументов.

Класс DevelopmentTeam должен иметь два метода экземпляра:

add_junior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем разработчика, и добавляющий их в число junior-разработчиков
add_senior() — метод, принимающий произвольное количество позиционных аргументов, каждый из которых является именем разработчика, и добавляющий их в число senior-разработчиков
Экземпляр класса DevelopmentTeam должен быть итерируемым объектом, элементами которого сперва являются все его junior-разработчики, а затем — все senior-разработчики. Junior-разработчики должны быть представлены в виде кортежей:

(<имя разработчика>, 'junior')
в то время как senior-разработчики — в виде кортежей:

(<имя разработчика>, 'senior')
Примечание 1. Разработчики в группах должны располагаться в том порядке, в котором они были добавлены.
"""

class DevelopmentTeam:

    JUNIORS = list()
    SENIORS = list()

    def __init__(self):
        pass

    def add_junior(self, *args):
        self.JUNIORS.extend(list(zip((*args, ), (('junior',) * len(args)))))

    def add_senior(self, *args):
        self.SENIORS.extend(list(zip((*args, ), (('senior',) * len(args)))))

    def __iter__(self):
        yield from self.JUNIORS
        yield from self.SENIORS

