"""
https://stepik.org/lesson/835206/step/14?auth=login&unit=838840

Декоратор @snake_case
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:

attrs — булево значение, по умолчанию равняется False
Декоратор должен переименовать все не магические методы в декорируемом классе, меняя их стиль написания c Camel Case и Lower Camel Case на Snake case. Параметр attrs должен определять, будут ли аналогичным образом переименованы атрибуты класса. Если он имеет значение True, стиль написания имен атрибутов класса должен поменяться с Camel Case и Lower Camel Case на Snake case, если False — остаться прежним.

Примечание 1. Гарантируется, что имена всех не магических методов и атрибутов в классе написаны в стилях Camel Case, LowerCamelCase или Snake Case.
"""
def camel_to_snake(s):
    return ''.join(['_'+c.lower() if c.isupper() and s.index(c) != 0 else c.lower() for c in s]).replace('__', '_')
def snake_case(attrs=False):
    def decorator(cls):
        methods = []
        att = []
        for attr in dir(cls):
            if callable(getattr(cls, attr)) and not attr.startswith('__'):
                methods.append(attr)
            if not callable(getattr(cls, attr)) and not attr.startswith('__'):
                att.append(attr)
        for method in methods:
            setattr(cls, camel_to_snake(method), getattr(cls, method))
            delattr(cls, method)
        if attrs:
            for att in att:
                setattr(cls, camel_to_snake(att), getattr(cls, att))
                delattr(cls, att)
        return cls
    return decorator
