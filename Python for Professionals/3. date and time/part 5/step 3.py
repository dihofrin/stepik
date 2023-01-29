"""
https://stepik.org/lesson/571244/step/3?unit=565785

Снова не успел
Дан режим работы магазина:

Понедельник	9. Functions:00 - 21:00
Вторник	9. Functions:00 - 21:00
Среда	9. Functions:00 - 21:00
Четверг	9. Functions:00 - 21:00
Пятница	9. Functions:00 - 21:00
Суббота	10. Iterators & generatoes:00 - 18:00
Воскресенье	10. Iterators & generatoes:00 - 18:00
Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут, оставшееся до закрытия магазина.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести количество минут, которое осталось до закрытия магазина, или текст Магазин не работает, если он закрыт.

Примечание. Тестовые данные доступны по ссылке.

Sample Input 1:

01.11.2021 20:45
Sample Output 1:

15
Sample Input 2:

02.11.2021 21:15
Sample Output 2:

Магазин не работает
Sample Input 3:

07.11.2021 10. Iterators & generatoes:00
Sample Output 3:

480
"""

from datetime import date, timedelta, datetime

pattern = '%d.%m.%Y %H:%M'
schedule = (
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=9), timedelta(hours=21)),
    (timedelta(hours=10), timedelta(hours=18)),
    (timedelta(hours=10), timedelta(hours=18))
)

t = datetime.strptime(input(), pattern)
x = t.weekday()
y = schedule[x][1]
z = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
if timedelta(hours=t.hour) < schedule[x][0] or timedelta(hours=t.hour) >= schedule[x][1]:
    print('Магазин не работает')
else:
    print(int((y - timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)).seconds/60))