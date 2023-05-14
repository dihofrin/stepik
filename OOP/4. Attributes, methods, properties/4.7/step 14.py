"""
https://stepik.org/lesson/794698/step/14?unit=797450

Класс Pet
Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:

name — имя домашнего животного
Экземпляр класса Pet должен иметь один атрибут:

name — имя домашнего животного
Класс Pet должен иметь три метода класса:

first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet
"""

class Pet:

    pets = []

    def __init__(self, name):
        self.name = name
        self.pets.append(self)

    @classmethod
    def first_pet(cls):
        if cls.pets:
            return cls.pets[0]
        return None

    @classmethod
    def last_pet(cls):
        if cls.pets:
            return cls.pets[-1]
        return None

    @classmethod
    def num_of_pets(cls):
        if cls.pets:
            return len(cls.pets)
        return 0