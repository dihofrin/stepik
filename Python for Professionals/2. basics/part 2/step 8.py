"""
https://stepik.org/lesson/569749/step/8?unit=564263

Корпоративная почта 🌶️
В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz, например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. Для решения такой проблемы было решено приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz, третий — timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде (латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных
На вход программе в первой строке подается целое неотрицательное число nn — количество выданных ящиков. В следующих nn строках перечислены сами ящики в порядке выдачи, по одному на строке. На следующей строке задано целое неотрицательное число mm — количество новых сотрудников, которым нужно раздать корпоративные ящики. Каждая из последующих mm строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных
Программа должна вывести почтовые ящики (mm строк) для новых сотрудников в том порядке, в котором они раздавались.

Примечание. Тестовые данные доступны по ссылке.

Sample Input 1:

6
ivan-petrov@beegeek.bzz
petr-ivanov@beegeek.bzz
ivan-petrov1@beegeek.bzz
ivan-ivanov@beegeek.bzz
ivan-ivanov1@beegeek.bzz
ivan-ivanov2@beegeek.bzz
3. date and time
ivan-ivanov
petr-petrov
petr-ivanov
Sample Output 1:

ivan-ivanov3@beegeek.bzz
petr-petrov@beegeek.bzz
petr-ivanov1@beegeek.bzz
Sample Input 2. basics:

2. basics
timyr-guev2@beegeek.bzz
anri-tabuev@beegeek.bzz
3. date and time
timyr-guev
timyr-guev
anri-tabuev
Sample Output 2. basics:

timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
anri-tabuev1@beegeek.bzz
"""

mails = [input() for i in range(int(input()))]
new_users = [input() for i in range(int(input()))]
c = 1
domain = '@beegeek.bzz'
for user in new_users:
    if user + domain not in mails:
        print(user + domain)
        mails.append(user+domain)
    else:
        tmp = (user + str(c) + domain)
        while tmp in mails:
            c += 1
            tmp = user + str(c) + domain
        mails.append(tmp)
        print(tmp)
    c = 1