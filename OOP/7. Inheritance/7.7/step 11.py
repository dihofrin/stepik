"""
https://stepik.org/lesson/798679/step/11?unit=801642

Классы USADate и ItalianDate
1. Реализуйте класс USADate, описывающий дату в американском формате. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

year — год
month — месяц
day — день
Класс USADate должен иметь два метода экземпляра:

format() — метод, который возвращает строку, представляющую собой дату в формате MM-DD-YYYY
iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
2. Также реализуйте класс ItalianDate, описывающий дату в итальянском формате, конструктор которого принимает три аргумента:

year — год
month — месяц
day — день
Класс ItalianDate должен иметь два метода экземпляра:

format() — который возвращает строку, представляющую собой дату в формате DD/MM/YYYY
iso_format() — который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
"""

class USADate:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self):
        return f'{str(self.month).zfill(2)}-{str(self.day).zfill(2)}-{self.year}'

    def iso_format(self):
        return f'{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}'


class ItalianDate(USADate):

    def format(self):
        return f'{str(self.day).zfill(2)}/{str(self.month).zfill(2)}/{self.year}'


