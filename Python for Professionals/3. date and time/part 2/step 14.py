"""
https://stepik.org/lesson/570048/step/14?unit=564591

Функция print_good_dates()
Тимур считает дату «интересной», если её год совпадает с годом его рождения, а сумма номера месяца и номера дня равна его возрасту. Год рождения Тимура — 19921992, возраст — 2929 лет.

Реализуйте функцию print_good_dates(), которая принимает один аргумент:

dates — список дат (тип date)
Функция должна выводить «интересные» даты в порядке возрастания, каждую на отдельной строке, в формате  month_name DD, YYYY, где month_name — полное название месяца на английском.

Примечание 1. Если в функцию передается пустой список или список без интересных дат, функция ничего не должна выводить.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_good_dates(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.

Таблица форматирования
Sample Input 1:

dates = [date(1992, 10. Iterators & generators, 19), date(1991, 12, 6. Collections), date(1992, 9. Functions, 20)]
print_good_dates(dates)
Sample Output 1:

September 20, 1992
October 19, 1992
Sample Input 2:

dates = [date(1993, 9. Functions, 15), date(2021, 11, 2), date(2000, 7. Exceptions, 7. Exceptions)]
print_good_dates(dates)
Sample Output 2:
"""

from datetime import date

def print_good_dates(dates):
    good_dates = []
    for i in dates:
        if i.year == 1992 or i.month + i.day == 29:
            good_dates.append(i)
    if good_dates:
        for i in sorted(good_dates):
            print(i.strftime('%B %d, %Y'))