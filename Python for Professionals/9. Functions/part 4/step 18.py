"""
https://stepik.org/lesson/647292/step/18?unit=643926

Функция remove_marks()
Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:

text — произвольная строка
marks — набор символов
Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.

Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов данной функции.
"""

def remove_marks(text, marks):
    remove_marks.count += 1
    return ''.join(i for i in text if i not in marks)

remove_marks.count = 0
