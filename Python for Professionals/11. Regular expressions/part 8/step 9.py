"""
https://stepik.org/lesson/680266/step/9?unit=678924

Функция normalize_jpeg()
Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:

filename — название файла, имеющее расширение jpeg или jpg, которое может быть записано буквами произвольного регистра
Функция должна возвращать новое название файла с нормализованным расширением — jpg.
"""

from re import sub

def normalize_jpeg(filename):
    return sub(r'([Jj][Pp][Ee]?[Gg])$', r'jpg', filename)
