"""
https://stepik.org/lesson/640039/step/23?auth=login&unit=636559

Декоратор exception_decorator
Реализуйте декоратор exception_decorator, который возвращает

кортеж (value, 'Функция выполнилась без ошибок'), если декорируемая функция завершила свою работу без ошибок, где value — возвращаемое значение декорируемой функции
кортеж (None, 'При вызове функции произошла ошибка'), если при выполнении декорируемой функции возникла ошибка
"""

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs), 'Функция выполнилась без ошибок')
        except:
            return (None, 'При вызове функции произошла ошибка')
    return wrapper
