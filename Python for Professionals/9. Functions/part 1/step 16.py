"""
https://stepik.org/lesson/640035/step/16?unit=636555

Необычная сортировка 🌶️
Дана строка, содержащая латинские буквы и цифры. Напишите программу, которая сортирует символы в строке согласно следующим правилам:

все отсортированные строчные буквы стоят перед заглавными буквами
все отсортированные заглавные буквы стоят перед цифрами
все отсортированные нечетные цифры стоят перед четными
Формат входных данных
На вход программе подается строка, содержащая латинские буквы и цифры.

Формат выходных данных
Программа должна расположить символы в строке в соответствии с условием задачи и вывести полученный результат.

Примечание. Тестовые данные доступны по ссылке.

Sample Input 1:

Sorting1234
Sample Output 1:

ginortS1324
Sample Input 2:

n0tEast3rEgg
Sample Output 2:

aggnrsttEE30
Sample Input 3:

3DYrz34UXl
Sample Output 3:

lrzDUXY334
"""

word = input()
ups = [i for i in word if i.isupper()]
downs = [i for i in word if i.islower()]
digs = [i for i in word if i.isdigit()]
odds = [i for i in digs if int(i) % 2]
evens = [i for i in digs if not int(i) % 2]
print(*sorted(downs)+sorted(ups)+sorted(odds)+sorted(evens), sep='')