"""
https://stepik.org/lesson/860444/step/23?unit=864459

Класс MutableString
Реализуйте класс MutableString, наследника класса UserString, описывающий изменяемую строку. Процесс создания экземпляра класса MutableString должен совпадать с процессом создания экземпляра класса UserString.

Класс MutableString должен иметь три метода экземпляра:

lower() — метод, переводящий все символы изменяемой строки в нижний регистр
upper() — метод, переводящий все символы изменяемой строки в верхний регистр
sort() — метод, сортирующий символы изменяемой строки. Может принимать два необязательных именованных аргумента key и reverse, выполняющих ту же задачу, что и в функции sorted()
Экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.
"""


from collections import UserString
class MutableString(UserString):

    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))

    def __setitem__(self, key, value):
        data_as_list = list(self.data)
        data_as_list[key] = value
        self.data = ''.join(data_as_list)

    def __delitem__(self, key):
        data_as_list = list(self.data)
        del data_as_list[key]
        self.data = ''.join(data_as_list)
