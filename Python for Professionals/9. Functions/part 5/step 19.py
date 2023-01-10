"""
https://stepik.org/lesson/651459/step/19?unit=648165

Функция date_formatter()
Нередко в разных странах используются разные форматы дат. Рассмотрим часть из них:

код страны	формат даты
ru	DD.MM.YYYY
us	MM-DD-YYYY
ca	YYYY-MM-DD
br	DD/MM/YYYY
fr	DD.MM.YYYY
pt	DD-MM-YYYY
Реализуйте функцию date_formatter(), которая принимает один аргумент:

country_code — код страны
Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date) и возвращает строку с данной датой в формате страны с кодом country_code.
"""

from datetime import date
def date_formatter(country_code):
    d = {'ru': '%d.%m.%Y',
         'us': '%m-%d-%Y',
         'ca': '%Y-%m-%d',
         'br': '%d/%m/%Y',
         'fr': '%d.%m.%Y',
         'pt': '%d-%m-%Y', }
    def func(dat):
        return date.strftime(dat, d[country_code])
    return func