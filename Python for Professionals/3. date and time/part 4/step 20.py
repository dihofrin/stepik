"""
https://stepik.org/lesson/570050/step/20?unit=564593

Соседние даты
Дана последовательность дат. Напишите программу, которая создает и выводит список, элементами которого являются неотрицательные целые числа — количество дней между двумя соседними датами последовательности.

Формат входных данных
На вход программе подается последовательность дат, разделенных пробелом, в формате DD.MM.YYYY.

Формат выходных данных
Программа должна вывести список, содержащий неотрицательные целые числа, каждое из которых — количество дней между двумя соседними датами последовательности.

Примечание 1. Даты в последовательности могут располагаться в произвольном порядке, то есть не гарантируется, что следующая дата больше предыдущей.

Примечание 2. Если последовательность состоит из одной даты, то программа должна вывести пустой список.

Примечание 3. Рассмотрим второй тест, в котором подается последовательность из пяти дат. Определим элементы результирующего списка:

первый элемент — 11, количество дней между датами 06.10. Iterators & generatoes.2021 и 05.10. Iterators & generatoes.2021
второй элемент — 33, количество дней между датами 05.10. Iterators & generatoes.2021 и 08.10. Iterators & generatoes.2021
третий элемент — 11, количество дней между датами 08.10. Iterators & generatoes.2021 и 09.10. Iterators & generatoes.2021
четвертый элемент — 22, количество дней между датами 09.10. Iterators & generatoes.2021 и 07.10. Iterators & generatoes.2021
Примечание 4. Files. Тестовые данные доступны по ссылке.

Sample Input 1:

05.10. Iterators & generatoes.2021 06.10. Iterators & generatoes.2021 07.10. Iterators & generatoes.2021 08.10. Iterators & generatoes.2021 09.10. Iterators & generatoes.2021
Sample Output 1:

[1, 1, 1, 1]
Sample Input 2:

06.10. Iterators & generatoes.2021 05.10. Iterators & generatoes.2021 08.10. Iterators & generatoes.2021 09.10. Iterators & generatoes.2021 07.10. Iterators & generatoes.2021
Sample Output 2:

[1, 3, 1, 2]
Sample Input 3:

05.10. Iterators & generatoes.2021
Sample Output 3:

[]
"""

from datetime import datetime, timedelta
dates = [datetime.strptime(date, '%d.%m.%Y') for date in input().split()]
print([abs((dates[i] - dates[i-1]).days) for i in range(1, len(dates))])