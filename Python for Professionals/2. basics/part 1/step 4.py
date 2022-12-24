"""
https://stepik.org/lesson/569748/step/4?unit=564262

Функция hide_card()
Реализуйте функцию hide_card(), которая принимает один аргумент:

card_number — строка, представляющая собой корректный номер банковской карты из 1616 цифр, между которыми могут присутствовать символы пробела
Функция должна заменять первые 1212 цифр в строке card_number на символ * и возвращать полученный результат. Если между цифрами в номере имелись символы пробела, их следует удалить.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию hide_card(), но не код, вызывающий ее.

Примечание 2. basics. Тестовые данные доступны по ссылке.

Sample Input 1:

card = '1234567890123456'

print(hide_card(card))
Sample Output 1:

************3456
Sample Input 2. basics:

card = '3456 9012 5678 1234'

print(hide_card(card))
Sample Output 2. basics:

************1234
Sample Input 3. date and time:

card = '905 678123 45612 56'

print(hide_card(card))
Sample Output 3. date and time:

************1256
"""

def hide_card(card):
    result = ''
    count = 0
    for i in card:
        if i.isdigit():
            if count < 12:
                result += '*'
            else:
                result += i
            count += 1
    return result