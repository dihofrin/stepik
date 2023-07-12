"""
https://stepik.org/lesson/805785/step/17?unit=816644

Класс HistoryDict 🌶️
Реализуйте класс HistoryDict, описывающий словарь, который запоминает предыдущие значения по каждому ключу. При создании экземпляра класс должен принимать один аргумент:

data — словарь, определяющий начальный набор элементов экземпляра класса HistoryDict. Если не передан, начальный набор элементов считается пустым
Класс HistoryDict должен иметь пять методов экземпляра:

keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса HistoryDict
values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса HistoryDict
items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса HistoryDict в виде кортежей (<ключ>, <значение>)
history() — метод, принимающий в качестве аргумента ключ и возвращающий список, элементами которого являются все значения, которые когда-либо содержались в экземпляре класса HistoryDict по указанному ключу. Если данный ключ не содержится в экземпляре класса HistoryDict (был удален или никогда не добавлялся), метод должен вернуть пустой список
all_history() — метод, возвращающий словарь, ключами в котором являются ключи экземпляра класса HistoryDict, а значениями — списки, содержащие все значения, которые когда-либо содержались по этим ключам
При передаче экземпляра класса HistoryDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса HistoryDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.

Наконец, экземпляр класса HistoryDict должен позволять получать и изменять значения своих элементов по их ключам, добавлять новые пары (ключ, значение) и удалять уже имеющиеся.

Примечание 1. Экземпляр класса HistoryDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса HistoryDict измениться  не должен.
"""

class HistoryDict:

    def __init__(self, data=()):
        self.data = dict(data) or {}
        self.hist_data = {k: [v] for k, v in self.data.items()}

    def keys(self):
        yield from self.data.keys()

    def __repr__(self):
        return f'{self.hist_data}'

    def values(self):
        yield from self.data.values()

    def items(self):
        yield from self.data.items()

    def history(self, key):
        return self.hist_data.get(key, [])

    def all_history(self):
        return self.hist_data

    def __len__(self):
        return len(self.hist_data)

    def __iter__(self):
        yield from self.hist_data

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.hist_data.setdefault(key, []).append(value)
        self.data[key] = value
    def __delitem__(self, item):
        del self.hist_data[item]
        del self.data[item]