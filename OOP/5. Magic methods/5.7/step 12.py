"""
https://stepik.org/lesson/805783/step/12?unit=808910

Класс RomanNumeral🌶️🌶️
Реализуйте класс RomanNumeral, описывающий число в римской системе счисления. При создании экземпляра класс должен принимать один аргумент:

number — число в римской системе счисления. Например, IV
Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:

<число в римской системе счисления>
Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому его значением должно являться целое число в десятичной системе счисления, которому он соответствует.

Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=.

Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания с помощью операторов + и - соответственно:

результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных
Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.
"""


class RomanNumeral:
    ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        i = 0
        num = 0
        while i < len(self.number):
            if i + 1 < len(self.number) and self.number[i:i + 2] in RomanNumeral.ROMAN:
                num += RomanNumeral.ROMAN[self.number[i:i + 2]]
                i += 2
            else:
                num += RomanNumeral.ROMAN[self.number[i]]
                i += 1
        return num

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number == other.number
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) > int(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) >= int(other)
        return NotImplemented

    def __add__(self, other):
        result = RomanNumeral.to_roman(int(self) + int(other))
        return RomanNumeral(result)

    def __sub__(self, other):
        result = RomanNumeral.to_roman(int(self) - int(other))
        return RomanNumeral(result)

    @staticmethod
    def to_roman(num):
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        thousands = m[num // 1000]
        hundreds = c[(num % 1000) // 100]
        tens = x[(num % 100) // 10]
        ones = i[num % 10]

        result = thousands + hundreds + tens + ones

        return result
