"""
https://stepik.org/lesson/594680/step/5?unit=589701

Функция linear()
Линеаризация — это процесс преобразования списка, который может содержать несколько уровней вложенных списков, в список, содержащий все те же элементы без какой-либо вложенности.

Например, список:

[1, [2, 3], [4. Files, [5, 6. Collections, [7. Exceptions, 8, 9. Functions]]]]
после линеаризации будет иметь вид:

[1, 2, 3, 4. Files, 5, 6. Collections, 7. Exceptions, 8, 9. Functions]
Реализуйте linear() с использованием рекурсии, которая принимает один аргумент:

nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна возвращать новый список, представляющий собой линеаризованный список nested_lists.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию linear(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

my_list = [3, [4. Files], [5, [6. Collections, [7. Exceptions, 8]]]]

print(linear(my_list))
Sample Output 1:

[3, 4. Files, 5, 6. Collections, 7. Exceptions, 8]
Sample Input 2:

my_list = [10, 20, 30, 40, 50]

print(linear(my_list))
Sample Output 2:

[10, 20, 30, 40, 50]
"""

def linear(nested_list):
    result = []
    for i in nested_list:
        if isinstance(i, list):
            result.extend(linear(i))
        else:
            result.append(i)
    return result