"""
https://stepik.org/lesson/796462/step/14?unit=799267

Класс HourClock
Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой. При создании экземпляра класс должен принимать один аргумент:

hours — количество часов. Если hours не является целым числом, принадлежащим диапазону [1; 12], должно быть возбуждено исключение ValueError с текстом:
Некорректное время
Класс HourClock должен иметь одно свойство:

hours — свойство, доступное для чтения и записи, возвращающее текущее количество часов. При изменении свойство должно проверять, что новое значение является целым числом, принадлежащим диапазону [1; 12], в противном случае должно быть возбуждено исключение ValueError с текстом:
Некорректное время
"""

class HourClock:

    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if not isinstance(hours, int) or hours < 1 or hours > 12:
            raise ValueError('Некорректное время')
        self._hours = hours

    hours = property(fget=get_hours, fset=set_hours)

try:
    HourClock(0)
except ValueError as e:
    print(e)