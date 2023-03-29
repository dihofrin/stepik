"""
https://stepik.org/lesson/680265/step/15?unit=678923

Функция abbreviate()
Аббревиатура — слово, образованное сокращением слова или словосочетания и читаемое по алфавитному названию начальных букв или по начальным звукам слов, входящих в него.

Реализуйте функцию abbreviate(), которая принимает один аргумент:

phrase — фраза
Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.

Примечание 1. В аббревиатуре должны присутствовать как начальные буквы слов, так и начальные буквы подслов, начинающихся с заглавной буквы, например, JavaScript Object Notation -> JSON.
"""
import re

pattern = r'[A-Z]|\b\w{1}'
def abbreviate(word: str) -> str:
    return ''.join(re.findall(pattern, word)).upper()

print(abbreviate('javaScript object notation'))