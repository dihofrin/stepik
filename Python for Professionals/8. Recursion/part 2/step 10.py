"""
https://stepik.org/lesson/637962/step/10?unit=634429

Функция triangle() 😰
Реализуйте функцию triangle() с использованием рекурсии, которая принимает один аргумент:

h — натуральное число
Функция должна выводить звездный треугольник с высотой h в соответствии со следующим примером:

*
**
***
****
*****
...
Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию triangle(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

triangle(3)
Sample Output 1:

*
**
***
Sample Input 2:

triangle(5)
Sample Output 2:

*
**
***
****
*****
"""

def triangle(h):
    if h:
        triangle(h-1)
        print('*'*h)