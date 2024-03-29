"""
https://stepik.org/lesson/594137/step/8?unit=589173

Функция number_of_frogs()
В первый год в пруду живет 7777 лягушек. Каждый год из пруда вылавливают 3030 лягушек, а оставшиеся размножаются, и их становится в три раза больше. Так, количество лягушек kk-й год  может быть описано формулой:

F_k = 3(F_{k-1} - 30)
F
k
​
 =3(F
k−1
​
 −30)

Реализуйте функцию number_of_frogs() с использованием рекурсии, которая принимает один аргумент:

year — натуральное число
Функция должна возвращать единственное число — количество лягушек в пруду в году year.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию number_of_frogs(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

print(number_of_frogs(2))
Sample Output 1:

141
Sample Input 2:

print(number_of_frogs(10. Iterators & generators))
Sample Output 2:

629901
Sample Input 3:

print(number_of_frogs(1))
Sample Output 3:

77
"""

def number_of_frogs(n):
    if n == 1:
        return 77
    return 3 * (number_of_frogs(n-1) - 30)