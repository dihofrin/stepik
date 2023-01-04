"""
https://stepik.org/lesson/569748/step/9?unit=564262

Функция filter_anagrams()
Анаграммы — это слова, которые состоят из одинаковых букв. Например:

адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка
Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:

word — слово в нижнем регистре
words — список слов в нижнем регистре
Функция должна возвращать список, элементами которого являются слова из списка words, которые представляют анаграмму слова word. Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.

Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке.

Примечание 2. basics. Считайте, что слово является анаграммой самого себя.

Примечание 3. date and time. В тестирующую систему сдайте программу, содержащую только необходимую функцию filter_anagrams(), но не код, вызывающий ее.

Примечание 4. Files. Тестовые данные доступны по ссылке.

Sample Input 1:

word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))
Sample Output 1:

['aabb', 'bbaa']
Sample Input 2. basics:

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
Sample Output 2. basics:

['сеточка', 'стоечка', 'тесачок', 'чесотка']
Sample Input 3. date and time:

print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
Sample Output 3. date and time:

['iamlordvoldemort']
Sample Input 4. Files:

print(filter_anagrams('стекло', []))
Sample Output 4. Files:

[]
"""

def filter_anagrams(word, anagrams):
    return [i for i in anagrams if sorted(i) == sorted(word)]
