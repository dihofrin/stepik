"""
https://stepik.org/lesson/594680/step/8?unit=589701

Функция dict_travel() 🌶️🌶️
Реализуйте функцию dict_travel(), которая принимает один аргумент:

nested_dicts — словарь, содержащий в качестве значений числа, строки или словари, которые, в свою очередь, так же содержат в качестве значений числа, строки или словари; вложенность может быть произвольной
Функция должна выводить все пары ключ-значение словаря nested_dicts, а также значения всех его дочерних словарей. При выводе значений дочерних словарей необходимо перечислять имена всех ключей, начиная с верхнего уровня, разделяя их точками.

Например, в словаре:

{'name': 'Arthur', 'grades': {'math': [4, 4], 'chemistry': [3, 4]}}
значение [4, 4] должно быть выведено в следующем формате:

grades.math: [4, 4]
Все пары ключ-значение должны быть расположены в лексикографическом порядке, каждая на отдельной строке.

Примечание 1. Гарантируется, что ключами в подаваемом в функцию словаре являются строки, содержащие только латинские буквы в нижнем регистре.

Примечание 2. Гарантируется, что ни один ключ в подаваемом в функцию словаре не является последовательностью других ключей. Другими словами, словарь не может иметь, например, следующий вид:

{'b.c': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию dict_travel(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылке.

Sample Input 1:

data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
Sample Output 1:

a: 1
b.a: 10
b.b: 20
b.c: 30
Sample Input 2:

data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)
Sample Output 2:

a: 100
b.a: 10
b.b: 20
b.c: 30
d: 1
Sample Input 3:

data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)
Sample Output 3:

b.a: 10
b.b.d: 40
b.b.e: 50
b.c: 30
"""

def dict_travel(nested_dicts):
    keys = sorted(nested_dicts)
    result = dict.fromkeys(keys)
    for k, v in nested_dicts.items():
        if isinstance(v, dict):
            dict_travel(v)
        else:
            result[k] = v
    return result

data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
print(dict_travel(data))