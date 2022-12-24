"""
https://stepik.org/lesson/569748/step/6?unit=564262

Функция is_valid()
Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:

состоит из 44, 55 или 66 символов
состоит только из цифр (0-90−9)
не содержит пробелов
Реализуйте функцию is_valid(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать значение True, если строка string представляет собой корректный PIN-код, или False в противном случае.

Примечание 1. Если в функцию передается пустая строка, функция должна возвращать значение False.

Примечание 2. basics. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_valid(), но не код, вызывающий ее.

Примечание 3. date and time. Тестовые данные доступны по ссылке.

Sample Input 1:

print(is_valid('4367'))
Sample Output 1:

True
Sample Input 2. basics:

print(is_valid('92134'))
Sample Output 2. basics:

True
Sample Input 3. date and time:

print(is_valid('89abc1'))
Sample Output 3. date and time:

False
Sample Input 4:

print(is_valid('900876'))
Sample Output 4:

True
Sample Input 5:

print(is_valid('49 83'))
Sample Output 5:

False"""

def is_valid(pin):
    return pin.isdigit() and ' ' not in pin and len(pin) in [4, 5, 6]
