"""
https://stepik.org/lesson/860444/step/17?unit=864459

Класс EasyDict
Реализуйте класс EasyDict, наследника класса dict, описывающий словарь, значения элементов которого можно получать как по ключам ([key]), так и по одноименным атрибутам (.key). Процесс создания экземпляра класса EasyDict должен совпадать с процессом создания экземпляра класса dict.
"""

class EasyDict(dict):

    def __getattr__(self, attr):
        return self[attr]