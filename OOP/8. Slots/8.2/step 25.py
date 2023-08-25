"""
https://stepik.org/lesson/794703/step/25?unit=797455

Классы Weekday и NextDate
1. Реализуйте класс Weekday, описывающий перечисление с днями недели. Перечисление должно иметь семь элементов:

MONDAY — элемент со значением 0
TUESDAY — элемент со значением 1
WEDNESDAY — элемент со значением 2
THURSDAY — элемент со значением 3
FRIDAY — элемент со значением 4
SATURDAY — элемент со значением 5
SUNDAY — элемент со значением 6
2. Также реализуйте класс NextDate, позволяющий определять дату следующего дня недели, начиная с текущего дня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

today — дата текущего дня, представленная экземпляром класса date
weekday — день недели, представленный элементом перечисления Weekday
after_today — булево значение, по умолчанию равняется False
Параметр after_today должен определять, учитывается ли текущая дата при определении даты следующего дня недели. Если он имеет значение False, текущая дата не должна учитываться, если True — должна учитываться.

Класс NextDate должен иметь два метода экземпляра:

date() — метод, возвращающий дату следующего дня недели в виде экземпляра класса date
days_until() — метод, возвращающий количество дней до даты следующего дня недели
"""

from datetime import date
from enum import Enum

class Weekday(Enum):

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class NextDate:

    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        return date.fromordinal(self.today.toordinal() + self.days_until())

    def days_until(self):
        td = self.today.weekday()
        nd = self.weekday.value
        if td == nd:
            if self.after_today:
                return 0
            return 7
        return (7 - td + nd) % 7