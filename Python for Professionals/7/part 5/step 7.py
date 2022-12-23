"""
https://stepik.org/lesson/640052/step/7?thread=solutions&unit=636572

Функция is_good_password() 👀
Назовем пароль хорошим, если

его длина равна 99 или более символам
в нем присутствуют большие и маленькие буквы любого алфавита
в нем имеется хотя бы одна цифра
Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_good_password(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

print(is_good_password('41157082'))
Sample Output 1:

False
Sample Input 2:

print(is_good_password('мойпарольсамыйлучший'))
Sample Output 2:

False
Sample Input 3:

print(is_good_password('МойПарольСамыйЛучший111'))
Sample Output 3:

True
"""

def is_good_password(string):
    if len(string) > 8:
        if string.lower() != string:
            if [i for i in string if i in '0123456789']:
                return True
    return False