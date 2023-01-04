"""
https://stepik.org/lesson/518491/step/13?unit=510939

Средняя зарплата
Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников в различных компаниях. В первом столбце записано название компании, а во втором — зарплата очередного сотрудника:

company_name;salary
Atos;135000
ХайТэк;24400
Philax;128600
Инлайн Груп;43900
IBS;70600
Oracle;131600
Atos;91000
...
Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и выводит их названия, каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты, они должны быть расположены в лексикографическом порядке их названий.

Примечание 1. Средняя зарплата компании определяется как отношение суммы всех зарплат к их количеству.

Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, при этом кавычки не используются.

Примечание 3. Указанный файл доступен по ссылке.  https://stepik.org/media/attachments/lesson/518491/salary_data.csv

Примечание 4. Files. Начальная часть ответа выглядит так:

Информзащита
Форс
OFT group
...
Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
"""

import csv, os#, wget

# wget.download('https://stepik.org/media/attachments/lesson/518491/salary_data.csv')

with open('salary_data.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';')
    salaries = dict()
    for i in list(data)[1:]:
        salaries[i[0]] = salaries.get(i[0], []) + [int(i[1])]
    for i in sorted(salaries, key=lambda x: (sum(salaries[x])/len(salaries[x]), x)):
        print(i)

os.remove('salary_data.csv')