"""
https://stepik.org/lesson/805785/step/18?unit=816644


Класс MutableString 🌶️
Реализуйте класс MutableString, описывающий изменяемую строку. При создании экземпляра класс должен принимать один аргумент:

string — строка, определяющая начальное значение изменяемой строки. Если не передана, строка считается пустой
Класс MutableString должен иметь два метода экземпляра:

lower() — метод, переводящий все символы изменяемой строки в нижний регистр
upper() — метод, переводящий все символы изменяемой строки в верхний регистр
Экземпляр класса MutableString должен иметь неформальное строковое представление в следующем виде:

<текущее значение изменяемой строки>
Также экземпляр класса MutableString должен иметь формальное строковое представление в следующем виде:

MutableString('<текущее значение изменяемой строки>')
При передаче экземпляра класса MutableString в функцию len() должно возвращаться количество символов в нем.

Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом, то есть позволять перебирать свои символы, например, с помощью цикла for.

Также экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. Экземпляр класса MutableString должен поддерживать полноценные срезы, результатами которых должны быть новые изменяемые строки.

Наконец, экземпляры класса MutableString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса MutableString, представляющий конкатенацию исходных.
"""

class MutableString:

    def __init__(self, string=''):
        self.string = string


    def set_del(self, key, value=None):
        tmp = list(self.string)
        if value:
            tmp[key] = value
        else:
            del tmp[key]
        return tmp

    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()

    def __str__(self):
        return self.string

    def __repr__(self):
        return f'MutableString({repr(self.string)})'

    def __iter__(self):
        yield from self.string

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self.string + other.string)
        return NotImplemented

    def __getitem__(self, item):
        return MutableString(self.string[item])

    def __setitem__(self, key, value):
        self.string = ''.join(self.set_del(key, value))

    def __delitem__(self, key):
        self.string = ''.join(self.set_del(key))
