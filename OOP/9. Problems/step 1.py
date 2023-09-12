"""
https://stepik.org/lesson/864077/step/1?unit=923013

Функция anything()
Реализуйте функцию anything(), которая возвращает такой объект, результат сравнения с которым c помощью операторов ==, !=, >, <, >= и <= всегда равен True.
"""


class MostTrueClassInTheWorld:

    def __eq__(self, other):
        return True

    __ne__ = __ge__ = __le__ = __gt__ = __lt__ = __eq__

def anything():
    return MostTrueClassInTheWorld()

