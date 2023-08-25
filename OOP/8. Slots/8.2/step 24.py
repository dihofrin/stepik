"""
https://stepik.org/lesson/794703/step/24?unit=797455

Класс Seasons
Реализуйте класс Seasons, описывающий перечисление с временами года. Перечисление должно иметь четыре элемента:

WINTER — элемент со значением 1
SPRING — элемент со значением 2
SUMMER — элемент со значением 3
FALL — элемент со значением 4
Элемент перечисления должен иметь один метод:

text_value() — метод, принимающий в качестве аргумента код страны en или ru и возвращающий строковое значение элемента в зависимости от переданного аргумента. Для WINTER en и ru значениями являются winter и зима соответственно, для SPRING — spri
"""

from enum import Enum

class Seasons(Enum):

    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, code):
        translations = {
            "WINTER": {"en": "winter", "ru": "зима"},
            "SPRING": {"en": "spring", "ru": "весна"},
            "SUMMER": {"en": "summer", "ru": "лето"},
            "FALL": {"en": "fall", "ru": "осень"}
        }
        return translations[self.name][code]
