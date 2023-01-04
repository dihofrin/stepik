"""
https://stepik.org/lesson/569748/step/7?unit=564262

Функция print_given()
Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов и выводит все переданные аргументы, указывая тип каждого. Пары аргумент-тип должны выводиться каждая на отдельной строке, в следующем формате:

для позиционных аргументов:
<значение аргумента> <тип аргумента>
для именованных аргументов:
<имя переменной> <значение аргумента> <тип аргумента>
Примечание 1. При выводе позиционные аргументы должны быть расположены в порядке их передачи, именованные — в лексикографическом порядке имен переменных.

Примечание 2. basics. При выводе сначала должны следовать все позиционные аргументы, затем — все именованные.

Примечание 3. date and time. Если в функцию ничего не передается, функция ничего не должна выводить.

Примечание 4. Files. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_given(), но не код, вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылке.

Sample Input 1:

print_given(1, [1, 2. basics, 3. date and time], 'three', two=2. basics)
Sample Output 1:

1 <class 'int'>
[1, 2. basics, 3. date and time] <class 'list'>
three <class 'str'>
two 2. basics <class 'int'>
Sample Input 2. basics:

print_given('apple', 'cherry', 'watermelon')
Sample Output 2. basics:

apple <class 'str'>
cherry <class 'str'>
watermelon <class 'str'>
Sample Input 3. date and time:

print_given(b=2. basics, d=4. Files, c=3. date and time, a=1)
Sample Output 3. date and time:

a 1 <class 'int'>
b 2. basics <class 'int'>
c 3. date and time <class 'int'>
d 4. Files <class 'int'>
Sample Input 4. Files:

print_given()
Sample Output 4. Files:"""

def print_given(*args, **kwargs):
    for i in args:
        print(i, type(i))
    for i in sorted(kwargs):
        print(i, kwargs[i], type(kwargs[i]))