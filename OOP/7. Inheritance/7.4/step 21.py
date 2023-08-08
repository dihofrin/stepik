"""
https://stepik.org/lesson/860444/step/21?unit=864459

Класс ValueDict
Реализуйте класс ValueDict, наследника класса dict, описывающий словарь c дополнительным функционалом. Процесс создания экземпляра класса ValueDict должен совпадать с процессом создания экземпляра класса dict.

Класс ValueDict должен иметь два метода экземпляра:

key_of() — метод, принимающий в качестве аргумента объект value и возвращающий первый ключ экземпляра класса ValueDict, имеющий значение value. Если такого ключа нет, метод должен вернуть None.
keys_of() — метод, принимающий в качестве аргумента объект value и возвращающий итерируемый объект, элементами которого являются все ключи экземпляра класса ValueDict, имеющие значение value
"""

class ValueDict(dict):

    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k

    def keys_of(self, value):
        return [item for item in self if self[item] == value]
