"""
https://stepik.org/lesson/805783/step/11?unit=808910

Класс Temperature
Реализуйте класс Temperature, описывающий температуру в градусах по шкале Цельсия. При создании экземпляра класс должен принимать один аргумент:

temperature — температура в градусах по шкале Цельсия
Класс Temperature должен иметь один метод экземпляра:

to_fahrenheit() — метод, возвращающий температуру по шкале Фаренгейта
Класс Temperature должен иметь один метод класса:

from_fahrenheit() — метод, принимающий в качестве аргумента температуру по шкале Фаренгейта и возвращающий экземпляр класса Temperature, созданный на основе переданной температуры
Экземпляр класса Temperature должен иметь следующее неформальное строковое представление:

<температура в градусах по шкале Цельсия с округлением до двух знаков после запятой>°C
Также экземпляр класса Temperature должен поддерживать приведение к типам bool, int и float:

при приведении к типу bool значением экземпляра класса Temperature должно являться значение True, если его температура выше нуля, или False в противном случае
при приведении к типу int значением экземпляра класса Temperature должна являться его температура в виде целого числа с отброшенной дробной частью
при приведении к типу float значением экземпляра класса Temperature должна являться его температура в виде вещественного числа
"""

class Temperature:

    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return 9/5 * self.temperature + 32

    @classmethod
    def from_fahrenheit(cls, temperature):
        return Temperature(5/9 * (temperature - 32))

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'


    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)
