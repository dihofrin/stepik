"""
https://stepik.org/lesson/673155/step/10?unit=671418

Функция nonempty_lines()
Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:

file — название текстового файла, например, data.txt
Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла file с убранным символом переноса строки \n. Если строка содержит более
25
25 символов, она заменяется троеточием ....
"""

def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        file_lines = (line for line in f if not line.isspace())
        stripped = (line.strip('\n') for line in file_lines)
        swapped = ('...' if len(line) > 25 else line for line in stripped)
        yield from swapped


