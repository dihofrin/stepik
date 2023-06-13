"""
https://stepik.org/lesson/810855/step/13?unit=816646

Функция print_file_content()
Реализуйте функцию print_file_content(), которая принимает один аргумент:

filename — имя текстового файла
Функция должна выводить содержимое файла с именем filename. Если файла с данным именем нет в папке с программой, функция должна вывести текст:

Файл не найден
Примечание 1. Имя файла, передаваемого в функцию, уже содержит расширение.

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.
"""

def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(''.join(f.readlines()))
    except:
        print('Файл не найден')


