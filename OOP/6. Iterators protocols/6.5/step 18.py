"""
https://stepik.org/lesson/933767/step/18?unit=939666

Класс TreeBuilder 🌶️🌶️
Дерево — одна из наиболее широко распространённых структур данных в информатике, эмулирующая древовидную структуру в виде набора связанных узлов.

Элементы дерева называются узлами. На рисунке выше узлами являются значения 8, 3, 1, 6, 4, 7, 10, 14 и 13. Узлы без потомков называются листьями. На рисунке выше листьями являются значения 1, 4, 7 и 13.

Реализуйте класс TreeBuilder. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса TreeBuilder должен являться реентерабельным контекстным менеджером, который позволяет пошагово строить древовидную структуру данных (дерево).

Класс TreeBuilder должен иметь два метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект (лист) и добавляющий его в текущий узел дерева
structure() — метод, возвращающий структуру дерева в виде вложенных списков
Добавление узлов в дерево должно происходить с помощью оператора with. Узел считается текущим в рамках своего блока with. Если в узел не было добавлено ни одного листа, то этот узел не должен появляться в структуре дерева, возвращаемой методом structure().

Примечание 1. Структура дерева может быть произвольной, то есть узел может содержать другой узел, тот, в свою очередь, другой, и так далее.

Примечание 2. Гарантируется, что структура дерева не выводится внутри блоков with, то есть структура дерева выводится лишь после ее построения.
"""
# #my_first_solution
class TreeBuilder:
    level = -1
    tree = []

    def __init__(self):
        self.tmp = dict()

    def __enter__(self):
        type(self).level += 1
        self.tmp[type(self).level] = []
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.tmp[type(self).level]:
            del self.tmp[type(self).level]
        if type(self).level > 0:
            try:
                self.tmp[type(self).level - 1].append(self.tmp[type(self).level])
            except:
                pass
        else:
            type(self).tree.append(self.tmp[type(self).level])
        type(self).level -= 1

    def add(self, obj):
        if self.level < 0:
            type(self).tree.append(obj)
        else:
            self.tmp[type(self).level].append(obj)

    def structure(self):
        return type(self).tree


#best practices, using stack

# class TreeBuilder:
#     def __init__(self):
#         self.knots = [[]]
#
#     def __enter__(self):
#         self.knots.append([])
#
#     def __exit__(self, *args, **kwargs):
#         if self.knots[-1]:
#             self.knots[-2].append(self.knots[-1])
#         self.knots.pop()
#
#     def add(self, value):
#         self.knots[-1].append(value)
#
#     def structure(self):
#         return self.knots[-1]
