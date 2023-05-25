"""
https://stepik.org/lesson/805932/step/11?unit=809059

Класс Money
Реализуйте класс Money, описывающий денежную сумму в рублях. При создании экземпляра класс должен принимать один аргумент:

amount — количество денег
Экземпляр класса Money должен иметь следующее неформальное строковое представление:

<количество денег> руб.
Также экземпляр класса Money должен поддерживать унарные операторы + и -:

результатом унарного + должен являться новый экземпляр класса Money с неотрицательным количеством денег
результатом унарного - должен являться новый экземпляр класса Money с отрицательным количеством денег
"""

class Money:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'{self.amount} руб.'

    def __pos__(self):
        return Money(abs(self.amount))

    def __neg__(self):
        if self.amount > 0:
            return Money(self.amount * -1)
        return Money(self.amount)

money = Money(-100)

print(money)
print(+money)
print(-money)