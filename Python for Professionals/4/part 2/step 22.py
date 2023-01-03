"""
https://stepik.org/lesson/518491/step/22?unit=510939

Голодный студент 🌶️
Дима очень хочет поесть, но денег у него мало. Помогите ему определить самый дешевый продукт, а также магазин, в котором он продается. Вам доступен файл prices.csv, который содержит информацию о ценах продуктов в различных магазинах. В первом столбце записано название магазина, а в последующих — цена на соответствующий товар в этом магазине:

Магазин;Творог;Гречка;Рис;Бородинский хлеб;Яблоки;Пельмени;Овсяное печенье;Спагетти;Печеная фасоль;Мороженое;Фарш;Вареники;Картофель;Батончик
Пятерочка;69;133;129;83;141;90;72;123;149;89;88;106;54;84
Магнит;102;87;95;75;109;112;97;82;101;134;69;61;141;79
...
Напишите программу, которая определяет и выводит самый дешевый продукт и название магазина, в котором он продается, в следующем формате:

<название продукта>: <название магазина>
Если имеется несколько самых дешевых товаров, то следует вывести тот товар, чье название меньше в лексикографическом сравнении. Если один товар продается в нескольких магазинах по одной минимальной цене, то следует вывести тот магазин, чье название меньше в лексикографическом сравнении.

Примечание 1. Разделителем в файле prices.csv является точка с запятой, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке https://stepik.org/media/attachments/lesson/518491/prices.csv

Примечание 3. Пример вывода:

Клубничный йогурт: ВкусВилл
Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
"""

import csv, os

#import wget
#wget.download('https://stepik.org/media/attachments/lesson/518491/prices.csv')


with open('prices.csv', 'r', encoding='utf-8') as f:
    header, *reader = csv.reader(f, delimiter=';')
    m = 10**3
    mins = []
    for i in reader:
        s = int(min(i[1:], key=lambda x: int(x)))
        if s < m:
            m = s
    for i in range(1, len(header)):
        for j in reader:
            if int(j[i]) == m:
                mins.append([header[i], j[0]])
    mins = sorted(mins, key=lambda x: x[0])
    print(f'{mins[0][0]}: {mins[0][1]}')


os.remove('prices.csv')