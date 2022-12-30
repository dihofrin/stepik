"""
Функция get_all_values() 🌶️
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:

nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые, в свою очередь, так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
key — хешируемый объект
Функция должна определять все значения, которые соответствуют ключу key в словаре nested_dicts и всех его вложенных словарях, и возвращать их в виде множества. Если ключа key нет ни в одном словаре, функция должна вернуть пустое множество.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_all_values(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))
Sample Output 1:

4 5
Sample Input 2:

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))
Sample Output 2:

math videogames
Sample Input 3:

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'top_grade')

print(len(sorted(result)))
Sample Output 3:

0
"""

def get_all_values(nested_dicts, key):
    result = []
    if key in nested_dicts:
        result.append(nested_dicts[key])
    for k, v in nested_dicts.items():
        if isinstance(v, dict):
            result.extend(get_all_values(v, key))
    return set(result)