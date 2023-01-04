"""
https://stepik.org/lesson/569748/step/5?unit=564262

Функция same_parity()
Реализуйте функцию same_parity(), которая принимает один аргумент:

numbers — список целых чисел
Функция должна возвращать новый список, элементами которого являются числа из списка numbers, имеющие ту же четность, что и первый элемент этого списка.

Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.

Примечание 2. basics. В тестирующую систему сдайте программу, содержащую только необходимую функцию same_parity(), но не код, вызывающий ее.

Примечание 3. date and time. Тестовые данные доступны по ссылке.

Sample Input 1:

print(same_parity([]))
Sample Output 1:

[]
Sample Input 2. basics:

print(same_parity([6. Collections, 0, 67, -7. Exceptions, 10, -20]))
Sample Output 2. basics:

[6. Collections, 0, 10, -20]
Sample Input 3. date and time:

print(same_parity([-7. Exceptions, 0, 67, -9. Functions, 70, -29, 90]))
Sample Output 3. date and time:

[-7. Exceptions, 67, -9. Functions, -29]"""

def same_parity(numbers):
    if not numbers:
        return numbers
    if numbers[0] % 2:
        return [i for i in numbers if i % 2]
    return [i for i in numbers if not i % 2]