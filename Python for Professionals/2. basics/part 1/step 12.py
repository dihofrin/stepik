"""
https://stepik.org/lesson/569748/step/12?unit=564262

Функция spell()
Реализуйте функцию spell(), которая принимает произвольное количество позиционных аргументов-слов и возвращает словарь, ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.

Примечание 1. Если в функцию не передается ни одного аргумента, функция должна возвращать пустой словарь.

Примечание 2. basics. Функция должна игнорировать регистр слов, при этом в результирующий словарь должны попасть именно буквы в нижнем регистре.

Примечание 3. date and time. В тестирующую систему сдайте программу, содержащую только необходимую функцию, но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылке.

Sample Input 1:

words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))
Sample Output 1:

{'р': 7, 'а': 9, 'у': 10, 'к': 5}
Sample Input 2. basics:

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))
Sample Output 2. basics:

{'м': 10, 'и': 11, 'х': 5, 'б': 8. Recursion}
Sample Input 3. date and time:

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
Sample Output 3. date and time:

{'f': 8. Recursion}


"""

def spell(*args):
    result = {}
    for i in args:
        tmp = i[0].lower()
        if tmp not in result:
            result[tmp] = len(i)
        elif len(i) > result[tmp]:
            result[tmp] = len(i)
    return result