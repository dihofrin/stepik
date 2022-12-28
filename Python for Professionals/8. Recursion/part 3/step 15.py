"""
https://stepik.org/lesson/594137/step/15?unit=589173

Функция is_palindrome()
Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать значение True, если переданная строка является палиндромом, или False в противном случае.

Примечание 1. Палиндром — текст, одинаково читающийся в обоих направлениях.

Примечание 2. Пустая строка является палиндромом, как и строка, состоящая из одного символа.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_palindrome(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылке.

Sample Input 1:

print(is_palindrome('stepik'))
Sample Output 1:

False
Sample Input 2:

print(is_palindrome('level'))
Sample Output 2:

True
Sample Input 3:

print(is_palindrome('122333221'))
Sample Output 3:

True
"""

def is_palindrome(string):
    if len(string) < 2:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

print(is_palindrome('122333221'))