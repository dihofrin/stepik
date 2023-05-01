"""
https://stepik.org/lesson/794484/step/8?unit=797232

Декоратор @jsonify
Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON.
"""

import json
from functools import wraps

def jsonify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args))
    return wrapper
