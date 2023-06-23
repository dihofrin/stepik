"""
https://stepik.org/lesson/934146/step/19?unit=940038


Контекстный менеджер safe_write
Реализуйте контекстный менеджер safe_write с помощью декоратора @contextmanager, который принимает один аргумент:

filename — имя файла
Контекстный менеджер должен открывать файл с именем filename в режиме w и позволять выполнять с ним соответствующие операции. Причем если во время записи в файл было возбуждено какое-либо исключение, контекстный менеджер должен поглотить его, отменить все выполненные ранее записи в файл, если они были, вернуть файл в исходное состояние и проинформировать о возбужденном исключении выводом следующего текста:

Во время записи в файл было возбуждено исключение <тип исключения>
"""

from copy import deepcopy
from contextlib import contextmanager

@contextmanager
def safe_write(filename):
    file_c = deepcopy(filename)
    file = open(filename, 'w')
    try:
        yield file
    except Exception as e:
        print(f'Во время записи в файл было возбуждено исключение {e}')
        return file_c
    except:
        raise


