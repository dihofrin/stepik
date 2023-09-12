"""
https://stepik.org/lesson/864077/step/2?unit=923013

Класс Vector
Реализуйте класс Vector, экземпляр которого представляет собой вектор произвольной размерности. Экземпляр класса Vector должен создаваться на основе собственных координат:

a = Vector(1, 2, 3)
b = Vector(3, 4, 5)
c = Vector(5, 6, 7, 8)
В качестве неформального строкового представления вектор должен иметь собственные координаты, заключенные в круглые скобки:

print(a)                       # (1, 2, 3)
print(b)                       # (3, 4, 5)
print(c)                       # (5, 6, 7, 8)
Векторы должны поддерживать между собой операции сложения, вычитания, произведения и нормирования:

print(a + b)                   # (4, 6, 8)
print(a - b)                   # (-2, -2, -2)
print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292
а также операции сравнения на равенство и неравенство:

print(a == Vector(1, 2, 3))    # True
print(a == Vector(4, 5, 6))    # False
При попытке выполнить какую-либо операцию с векторами разной размерности должно быть возбуждено исключение ValueError с текстом:

Векторы должны иметь равную длину
"""

class Vector:

    def __init__(self, *args):
        self.args = args


    def __str__(self):
        return f'({", ".join(str(arg) for arg in self.args)})'

    def __len__(self):
        return len(self.args)

    def norm(self):
        return sum((arg * arg for arg in self.args)) ** 0.5

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Векторы должны иметь равную длину')
        if isinstance(other, type(self)):
            return type(self)(*tuple((sum(arg) for arg in zip(self.args, other.args))))
        return NotImplemented


    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Векторы должны иметь равную длину')
        if isinstance(other, type(self)):
            return type(self)(*tuple(self.args[i] - other.args[i] for i in range(len(self.args))))
        return NotImplemented


    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError('Векторы должны иметь равную длину')
        if isinstance(other, type(self)):
            return sum(self.args[i] * other.args[i] for i in range(len(self.args)))
        return NotImplemented

    def __eq__(self, other):
        if len(self) != len(other):
            raise ValueError('Векторы должны иметь равную длину')
        if isinstance(other, type(self)):
            return self.args == other.args
        return NotImplemented

    def __ne__(self, other):
        if len(self) != len(other):
            raise ValueError('Векторы должны иметь равную длину')
        if isinstance(other, type(self)):
            return self.args != other.args
        return NotImplemented

vector1 = Vector(1, 2, 3)
vector2 = Vector(3, 4, 5)
vector3 = Vector(5, 6, 7, 8)

print(vector1 == Vector(1, 2, 3))
print(vector1 == Vector(4, 5, 6))
print(vector1 != vector2)