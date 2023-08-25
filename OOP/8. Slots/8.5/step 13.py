"""
https://stepik.org/lesson/835206/step/13?auth=login&unit=838840

Декоратор @singleton
Реализуйте декоратор @singleton для декорирования класса. Декоратор должен превращать декорируемый класс в синглтон, то есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.
"""

def singleton(cls):
    cls.instance = None
    def new_new(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance
    cls.__new__ = new_new
    return cls
