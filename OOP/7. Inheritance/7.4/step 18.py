"""
https://stepik.org/lesson/860444/step/18?unit=864459

Класс TwoWayDict
Реализуйте класс TwoWayDict, наследника класса UserDict, описывающий двунаправленный словарь, в который при добавлении пары ключ: значение также добавляется и пара значение: ключ. Процесс создания экземпляра класса TwoWayDict должен совпадать с процессом создания экземпляра класса UserDict.
"""

from collections import UserDict


class TwoWayDict(UserDict):

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        super().__setitem__(value, key)
