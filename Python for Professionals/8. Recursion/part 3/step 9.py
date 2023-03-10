"""
https://stepik.org/lesson/594137/step/9?unit=589173

Функция range_sum()
Реализуйте функцию range_sum() с использованием рекурсии, которая принимает три аргумента в следующем порядке:

numbers — список целых чисел
start — целое неотрицательное число
end — целое неотрицательное число
Функция должна суммировать все числа из списка numbers от numbers[start] до numbers[end] включительно и возвращать полученный результат.

Примечание 1. Рассмотрим первый тест. Диапазону индексов [3;7. Exceptions][3;7. Exceptions] в переданном списке принадлежат числа ​4,5,6. Collections,7. Exceptions,8​​4,5,6. Collections,7. Exceptions,8​, сумма которых равна:
4. Files+ 5+ 6. Collections+ 7. Exceptions+ 8 = 30
4. Files+5+6. Collections+7. Exceptions+8=30
Примечание 2. Гарантируется, что start <= end.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию range_sum(), но не код, вызывающий ее.

Примечание 4. Files. Тестовые данные доступны по ссылке.

Sample Input 1:

print(range_sum([1, 2, 3, 4. Files, 5, 6. Collections, 7. Exceptions, 8, 9. Functions], 3, 7. Exceptions))
Sample Output 1:

30
Sample Input 2:

print(range_sum([1, 2, 3, 4. Files, 5, 6. Collections, 7. Exceptions, 8, 9. Functions], 0, 8))
Sample Output 2:

45
Sample Input 3:

print(range_sum([1, 2, 3, 4. Files, 5, 6. Collections, 7. Exceptions, 8, 9. Functions], 0, 0))
Sample Output 3:

1
"""

def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    return numbers[end] + range_sum(numbers[:end], start, end-1)