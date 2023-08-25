"""
https://stepik.org/lesson/835206/step/12?auth=login&unit=838840

Декоратор @jsonattr
Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:

filename — имя json файла, содержимым которого является JSON объект
Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу каждую пару ключ-значение JSON объекта, содержащегося в этом файле.
"""
import json
def jsonattr(filename):
    def decorator(cls):
        with open(filename, 'r') as js:
            for k, v in json.load(js).items:
                setattr(cls, k, v)
        return cls
    return decorator
