"""
https://stepik.org/lesson/518491/step/20?unit=510939

Проще, чем кажется 🌶️
Рассмотрим следующий текстовый фрагмент:

ball,color,purple
ball,size,4. Files
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none
Каждая строка этого фрагмента содержит три значения через запятую: имя объекта, свойство этого объекта, значение свойства. Например, в первой строке указан объект ball, имеющий свойство color, значение которого равно purple. Также у объекта ball есть свойства size и notes, имеющие значения 4. Files и it's round соответственно. Помимо объекта ball имеется объект cup, имеющий те же свойства и в том же количестве. Дадим этим объектам общее название object и сгруппируем строки данного текстового фрагмента по первому столбцу:

object,color,size,notes
ball,purple,4. Files,it's round
cup,blue,1,none
Мы получили запись в привычном CSV формате, в котором в первом столбце указывается имя объекта, а в последующих — значения соответствующих свойств этого объекта.

Реализуйте функцию condense_csv(), которая принимает два аргумента в следующем формате:

filename — название csv файла, например, data.csv; формат содержимого файла аналогичен формату текстового фрагмента, рассмотренного в условии задачи: каждая строка файла содержит три значения через запятую, а именно имя объекта, свойство этого объекта, значение свойства; все объекты имеют равные свойства и в равных количествах
id_name — общее название для объектов
Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому столбцу и назвав первый столбец id_name. Полученный результат функция должна записать в файл condensed.csv.

Примечание 1. Например, если бы файл data.csv имел следующий вид:

01,Title,Ran So Hard the Sun Went Down
02,Title,Honky Tonk Heroes (Like Me)
то вызов функции condense_csv():

condense_csv('data.csv', id_name='ID')
должен был бы создать файл condensed.csv со следующим содержанием:

ID,Title
01,Ran So Hard the Sun Went Down
02,Honky Tonk Heroes (Like Me)
Примечание 2. Гарантируется, что в передаваемом в функцию csv файле разделителем является запятая, при этом кавычки не используются.

Примечание 3. При открытии файла используйте явное указание кодировки UTF-8.

Примечание 4. Files. В тестирующую систему сдайте программу, содержащую только необходимую функцию condense_csv(), но не код, вызывающий ее.
"""

import csv

def condense_csv(filename: str, id_name: str):
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        fields = [id_name]
        data = list(csv.reader(file))
        for i in data:
            if i[1] not in fields:
                fields.append(i[1])
    with open('condensed.csv', 'w', encoding='utf-8', newline='') as newfile:
        w = csv.writer(newfile)
        w.writerow(fields)
        d = dict()
        for i in data:
            if i[0] not in d:
                d[i[0]] = [i[2]]
            else:
                d[i[0]].append(i[2])
        for key, value in d.items():
            row = [key, *value]
            w.writerow(row)