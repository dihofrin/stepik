"""
https://stepik.org/lesson/793864/step/16?unit=796596

Класс BankAccount
Реализуйте класс BankAccount, описывающий банковский счет. При создании экземпляра класс должен принимать один аргумент:

balance — баланс счета, по умолчанию имеет значение 0
Экземпляр класса BankAccount должен иметь один атрибут:

_balance — баланс счета
Класс BankAccount должен иметь четыре метода экземпляра:

get_balance() — метод, возвращающий актуальный баланс счета
deposit() — метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount
withdraw() — метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount. Если amount превышает количество средств на балансе счета, метод должен возбуждать исключение ValueError с сообщением:
На счете недостаточно средств
transfer() — метод, принимающий в качестве аргументов банковский счет account и число amount. Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на amount. Если amount превышает количество средств на балансе текущего счета, метод должен возбуждать исключение ValueError с сообщением:
На счете недостаточно средств
Примечание 1. Числами будем считать экземпляры классов int и float.
"""

class BankAccount:

    def __init__(self, balance=0):
        self._balance = balance


    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Amount should be positive number')
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Amount should be positive number')
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount
        return self._balance

    def transfer(self, account, amount):
        if amount > self._balance:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount
        account._balance += amount


