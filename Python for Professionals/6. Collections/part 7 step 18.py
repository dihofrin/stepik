"""
https://stepik.org/lesson/590120/step/18?unit=585064

А сколько стоит курс?
Тимур живет в мире, в котором цена товара определяется как сумма Unicode кодов букв его названия. Буквенным обозначением данной валюты являются две заглавные латинские буквы UC. Например, ручка в его мире стоит:

1088 + 1091 + 1095 + 1082 + 1072 = 5428 \,\, \mathrm{UC}
1088+1091+1095+1082+1072=5428UC
Тимур составляет список покупок, но так как на его клавиатуре перестал работать блок с цифрами, то вместо указания количества товара числом, он добавляет его в список столько раз, сколько планирует купить. Все товары Тимур записывает в нижнем регистре через запятую.

Напишите программу, которая группирует одинаковые товары из данного списка покупок и определяет стоимость каждой группы.

Формат входных данных
На вход программе подается последовательность товаров, разделенных запятой без пробелов.

Формат выходных данных
Программа должна сгруппировать одинаковые товары, определить общую стоимость каждой группы и вывести полученный результат. Товары должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:

<товар>: <цена за единицу товара> UC x <количество товаров в группе> = <общая стоимость группы> UC
Примечание 1. Программа должна добавлять нужное количество пробелов, если название товара имеет меньшую длину, чем другие.

Примечание 2. Получить Unicode код символа можно с помощью функции ord().
"""

from collections import Counter

def uc(word):
    return sum(ord(i) for i in word if i.isalpha())

words = input().split(',')
s = sorted(Counter(words).items())
m = len(max(words, key=len))

for key, value in s:
    print(f"{key: <{m}}: {uc(key)} UC x {value} = {uc(key)*value} UC")