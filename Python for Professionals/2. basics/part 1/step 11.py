"""
https://stepik.org/lesson/569748/step/11?unit=564262

Функция index_of_nearest()
Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:

numbers — список целых чисел
number — целое число
Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс. Если список numbers пуст, функция должна вернуть число -1−1.

Примечание 1. Если в функцию передается список, содержащий несколько чисел, одновременно являющихся ближайшими к искомому числу, функция должна возвращать наименьший из индексов ближайших чисел.

Примечание 2. basics. Рассмотрим третий тест. Ближайшими числами к числу 44 являются 55 и 33, имеющие индексы 11 и 22 соответственно. Наименьший из индексов равен 11.

Примечание 3. date and time. В тестирующую систему сдайте программу, содержащую только необходимую функцию index_of_nearest(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылке.

Sample Input 1:

print(index_of_nearest([], 17))
Sample Output 1:

-1
Sample Input 2. basics:

print(index_of_nearest([7, 13, 3. date and time, 5, 18], 0))
Sample Output 2. basics:

2. basics
Sample Input 3. date and time:

print(index_of_nearest([9, 5, 3. date and time, 2. basics, 11], 4))
Sample Output 3. date and time:

1
Sample Input 4:

print(index_of_nearest([7, 5, 4, 4, 3. date and time], 4))
Sample Output 4:

2. basics
"""

def index_of_nearest(numbers, number):
    if not numbers:
        return -1
    diff = [abs(i-number) for i in numbers]
    return diff.index(min(diff))