"""
https://stepik.org/lesson/569748/step/13?unit=564262

Функция choose_plural() 🌶️🌶️
Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:

amount — натуральное число, количество
declensions — кортеж из трех вариантов склонения существительного
Функция должна возвращать строку, полученную путем объединения подходящего существительного из кортежа declensions и количества amount, в следующем формате:

<количество> <существительное>
Примечание 1. Передаваемый в функцию кортеж легко составить по мнемоническому правилу: один, два, пять. Например:

для слова «арбуз»: арбуз, арбуза, арбузов
для слова «рубль»: рубль, рубля, рублей
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию choose_plural(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.

Sample Input 1:

print(choose_plural(21, ('пример', 'примера', 'примеров')))
Sample Output 1:

21 пример
Sample Input 2:

print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
Sample Output 2:

92 гвоздя
Sample Input 3:

print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
Sample Output 3:

8 яблок
"""

def choose_plural(amount, declensions):
    if str(amount).endswith('0'):
        return ' '.join((str(amount), declensions[2]))
    if amount in range (10, 20) or str(amount).endswith('12') or str(amount).endswith('13') or str(amount).endswith('14'):
        return ' '.join((str(amount), declensions[2]))
    if str(amount).endswith('1'):
        return ' '.join((str(amount), declensions[0]))
    if str(amount).endswith('2') or str(amount).endswith('3') or str(amount).endswith('4'):
        return ' '.join((str(amount), declensions[1]))
    return ' '.join((str(amount), declensions[2]))