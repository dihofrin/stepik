"""
https://stepik.org/lesson/569748/step/8?unit=564262

Функция convert()
Реализуйте функцию convert(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать строку string:

полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.

Примечание 2. basics. В тестирующую систему сдайте программу, содержащую только необходимую функцию convert(), но не код, вызывающий ее.

Примечание 3. date and time. Тестовые данные доступны по ссылке.

Sample Input 1:

print(convert('BEEgeek'))
Sample Output 1:

beegeek
Sample Input 2. basics:

print(convert('pyTHON'))
Sample Output 2. basics:

PYTHON
Sample Input 3. date and time:

print(convert('pi31415!'))
Sample Output 3. date and time:

pi31415!"""

def convert(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isalpha():
            if i.islower():
                lower += 1
            if i.isupper():
                upper += 1
    return s.upper() if upper > lower else s.lower()