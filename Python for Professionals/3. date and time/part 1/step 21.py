"""
https://stepik.org/lesson/609341/step/21?unit=604560

Функция get_date_range()
Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. Если start > end, функция должна вернуть пустой список.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_date_range(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:

date1 = date(2021, 10. Iterators & generators, 1)
date2 = date(2021, 10. Iterators & generators, 5)

print(*get_date_range(date1, date2), sep='\n')
Sample Output 1:

2021-10. Iterators & generators-01
2021-10. Iterators & generators-02
2021-10. Iterators & generators-03
2021-10. Iterators & generators-04
2021-10. Iterators & generators-05
Sample Input 2:

date1 = date(2019, 6. Collections, 5)
date2 = date(2019, 6. Collections, 5)

print(get_date_range(date1, date2))
Sample Output 2:

[datetime.date(2019, 6. Collections, 5)]
"""

from datetime import date

def get_date_range(start, end):
    if start > end:
        return list()
    return [date.fromordinal(i) for i in range(date.toordinal(start), date.toordinal(end)+1)]