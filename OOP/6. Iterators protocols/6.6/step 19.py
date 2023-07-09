"""
https://stepik.org/lesson/934146/step/19?unit=940038


Контекстный менеджер safe_write
Реализуйте контекстный менеджер safe_write с помощью декоратора @contextmanager, который принимает один аргумент:

filename — имя файла
Контекстный менеджер должен открывать файл с именем filename в режиме w и позволять выполнять с ним соответствующие операции. Причем если во время записи в файл было возбуждено какое-либо исключение, контекстный менеджер должен поглотить его, отменить все выполненные ранее записи в файл, если они были, вернуть файл в исходное состояние и проинформировать о возбужденном исключении выводом следующего текста:

Во время записи в файл было возбуждено исключение <тип исключения>
"""

from contextlib import contextmanager


@contextmanager
def safe_write(filename):
    f = open(filename, 'w')
    x = open(filename + 'r', 'w')
    try:
        x = x.write(f)
        yield f
    except Exception as e:
        print(f'Во время записи в файл было возбуждено исключение {type(e).__name__}')
        f = f.write(x)
        return f
    finally:
        x.close()
        f.close()


with safe_write('undertale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('undertale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
    raise ValueError

with open('undertale.txt') as file:
    print(file.read())