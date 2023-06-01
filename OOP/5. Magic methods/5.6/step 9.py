"""
https://stepik.org/lesson/805787/step/9?unit=808914

Класс Calculator
Реализуйте класс Calculator, экземпляры которого позволяют выполнять различные арифметические операции с двумя числами. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса Calculator должен являться вызываемым объектом и принимать три аргумента:

a — число
b — число
operation — один из символов +, -, * и /
Если operation равняется +, экземпляр класса Calculator должен вернуть сумму a и b, если - — разность a и b, если * — произведение a и b, если / — частное a и b. При попытке выполнить деление на ноль должно быть возбуждено исключение ValueError с текстом:

Деление на ноль невозможно
Примечание 1. Числами будет считать экземпляры классов int и float.
"""

class Calculator:

    def __call__(self, a, b, operation):
        match operation:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                try:
                    return a / b
                except:
                    pass


calculator = Calculator()

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))
