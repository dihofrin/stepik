"""
https://stepik.org/lesson/594680/step/4?unit=589701

Функция recursive_sum()
Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:

nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат. Если список nested_lists пуст, функция должна вернуть число 00.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию recursive_sum(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))
Sample Output 1:

24
Sample Input 2:

my_list = []

print(recursive_sum(my_list))
Sample Output 2:

0
"""
s = 0
def recursive_sum(nested_lists):
    global s
    if type(nested_lists) == int:
        s += nested_lists
    else:
        for i in nested_lists:
            recursive_sum(i)
    return s
