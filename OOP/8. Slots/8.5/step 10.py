"""
https://stepik.org/lesson/835206/step/10?auth=login&unit=838840

Декоратор @track_instances
Реализуйте декоратор @track_instances для декорирования класса. Декоратор должен добавлять декорируемому классу атрибут instances, содержащий список всех созданных экземпляров этого класса.
"""
from functools import wraps
def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = new_init

    return cls
