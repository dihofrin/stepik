"""
https://stepik.org/lesson/590035/step/21?unit=584967

Вам доступен список кортежей staff_broken с данными о сотрудниках некоторой компании. Первым элементом кортежа является название отдела, вторым — имя и фамилия сотрудника, работающего в этом отделе. Некоторые сотрудники могут встречаться в списке несколько раз.

Дополните приведенный ниже код, чтобы он сгруппировал сотрудников по соответствующим отделам и вывел названия всех отделов, указав для каждого имена и фамилии его сотрудников. Отделы, а также имена и фамилии сотрудников в этих отделах, должны быть расположены в лексикографическом порядке, каждый на отдельной строке, в следующем формате:

<отдел>: <имя> <фамилия>, <имя> <фамилия>, ...
Примечание. Начальная часть ответа выглядит так:

Accounting: Aaron Ferguson, Ann Bell, Brenda Davis, Casey Jenkins, Craig Wood, Dale Houston, Edna Cunningham, Gloria Higgins, James Wilkins, Jane Jackson, John Watts, Kay Scott, Kimberly Reynolds, Linda Hudson, Michelle Wright, Rosemary Garcia, Steven Diaz
Developing: Arlene Gibson, Deborah George, Joyce Rivera, Miguel Norris, Nicole Watts, Thomas Porter, Wilma Woods
...
"""

from collections import defaultdict

staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'), ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'), ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'), ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'), ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'), ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'), ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'), ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Dale Houston')]

s = defaultdict(list)
for i in staff_broken:
    if i[1] not in s[i[0]]:
        s[i[0]].append(i[1])
for i in sorted(s):
    print(f'{i}:', ', '.join(sorted(s[i])))

