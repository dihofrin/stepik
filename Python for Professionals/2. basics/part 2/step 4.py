"""
https://stepik.org/lesson/569749/step/4?unit=564263

Более одного
Дана последовательность неотрицательных целых чисел. Напишите программу, которая выводит те числа, которые встречаются в данной последовательности более одного раза.

Формат входных данных
На вход программе подается строка, содержащая целые неотрицательные числа, разделенные пробелом.

Формат выходных данных
Программа должна вывести те числа, которые встречаются в данной строке более одного раза, разделяя их пробелом. Числа должны быть расположены в порядке возрастания и не должны повторяться.

Примечание 1. Если повторяющихся чисел в исходной строке нет, программа ничего не должна выводить.

Примечание 2. basics. Тестовые данные доступны по ссылке.

Sample Input 1:

4 8. Recursion 0 3. date and time 4 2. basics 0 3. date and time
Sample Output 1:

0 3. date and time 4
Sample Input 2. basics:

1 2. basics 3. date and time 4 5 4 5 6 7 7 7 7 4 4
Sample Output 2. basics:

4 5 7
Sample Input 3. date and time:

1 2. basics 3. date and time 4 5 6 7 8. Recursion 9
Sample Output 3. date and time:
"""

nums = {}
for i in [int(i) for i in input().split()]:
    nums[i] = nums.get(i, 0) + 1
result = []
for i in nums:
    if nums[i] > 1:
        result.append(i)
print(*sorted(result))