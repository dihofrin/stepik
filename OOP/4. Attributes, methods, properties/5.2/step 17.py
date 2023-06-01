"""
https://stepik.org/lesson/805770/step/17?unit=808895

Класс PhoneNumber
Реализуйте класс PhoneNumber, описывающий телефонный номер. При создании экземпляра класс должен принимать один аргумент:

phone_number — телефонный номер, представляющий строку из десяти цифр в одном из следующих форматов:
dddddddddd
ddd ddd dddd
Экземпляр класса PhoneNumber должен иметь следующее формальное строковое представление:

PhoneNumber('<телефонный номер в формате dddddddddd>')
И следующее неформальное строковое представление:

<телефонный номер в формате (ddd) ddd-dddd>
"""


class PhoneNumber:

    def __init__(self, phone_number):
        self.phone_number = phone_number


    def __str__(self):
        phone_number = ''.join(i for i in self.phone_number if i.isdigit())
        return f'({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}'

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{"".join(i for i in self.phone_number if i.isdigit())}\')'

