"""
https://stepik.org/lesson/886253/step/25?unit=890908

Функция limited_hash() 🌶️
Реализуйте функцию limited_hash(), которая принимает три аргумента в следующем порядке:

left — целое число
right — целое число
hash_function — хеш-функция, по умолчанию равняется встроенной функции hash()
Функция должна возвращать новую функцию, которая принимает в качестве аргумента произвольный объект, вычисляет его хеш-значение с помощью функции hash_function(), преобразует его в число, принадлежащее диапазону [left; right], и возвращает полученный результат.

Если вычисленное хеш-значение уже принадлежит диапазону [left; right], то функция должна возвращать его без преобразования. Если вычисленное хеш-значение равняется right + 1, то функция перед возвратом должна преобразовать его в left, если right + 2 — в left + 1, если right + 3 — в left + 2, и так далее. Аналогичные преобразования, но в другую сторону, должны выполняться для хеш-значений, которые меньше left. Преобразования должны выполняться циклично при очередном выходе из диапазона.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию limited_hash(), но не код, вызывающий ее.
"""

def limited_hash(left, right, hash_function=hash):
    def func(obj):
        r = range(left, right+1)
        if hash_function(obj) in r:
            return hash_function(obj)
        return left + (hash_function(obj)-right-1)%(right-left+1)
    return func


# better solution

# def limited_hash(left, right, hash_function=hash):
#     def func(obj):
#         return left + (hash_function(obj)-right-1)%(right-left+1)
#     return func
