"""
https://stepik.org/lesson/640164/step/6?thread=solutions&unit=636683

Я в аду?
Напишите программу, которая в заданном тексте находит все телефонные номера, соответствующие следующим форматам:

7-ddd-ddd-dd-dd
8-ddd-dddd-dddd
где d — цифра от 0 до 9.

Формат входных данных
На вход программе подается строка произвольного содержания.
"""

import re

regex = r'\d{8}|(\d{2}[-\.]?){3}\d{2}|(\d{2}---){3}\d{2}'
