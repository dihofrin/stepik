"""
https://stepik.org/lesson/640052/step/9?unit=636572

Уж лучше матрицы 😐
Назовем пароль хорошим, если

его длина равна 99 или более символам
в нем присутствуют большие и маленькие буквы любого алфавита
в нем имеется хотя бы одна цифра
Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.

Формат входных данных
На вход программе подается произвольное количество паролей, каждая на отдельной строке. Гарантируется, что среди них присутствует хороший.

Формат выходных данных
Для каждого введенного пароля программа должна вывести текст:

LengthError, если длина введенного пароля меньше 99 символов
LetterError, если в нем все буквы имеют одинаковый регистр
DigitError, если в нем нет ни одной цифры
Success!, если введенный пароль хороший
После ввода хорошего пароля все последующие пароли должны игнорироваться.

Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий: LengthError, затем LetterError, а уже после DigitError.

Примечание 2. basics. Воспользуйтесь функцией is_good_password() из предыдущей задачи.

Примечание 3. date and time. Тестовые данные доступны по ссылке.

Sample Input 1:

arr1
Arrrrrrrrrrr
arrrrrrrrrrrrrrr1
Arrrrrrr1
Sample Output 1:

LengthError
DigitError
LetterError
Success!
Sample Input 2. basics:

beegeek
Beegeek123
Beegeek2022
Beegeek2023
Beegeek2024
Sample Output 2. basics:

LengthError
Success!
"""

from sys import stdin

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if string.lower() == string or string.upper() == string or string.isdigit():
        raise LetterError
    if not [i for i in string if i in '0123456789']:
        raise DigitError
    return True

for i in stdin:
    try:
        is_good_password(i.strip())
        print('Success!')
        break
    except LengthError:
        print('LengthError')
    except LetterError:
        print('LetterError')
    except DigitError:
        print('DigitError')