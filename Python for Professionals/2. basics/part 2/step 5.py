"""
https://stepik.org/lesson/569749/step/5?unit=564263

Максимальная группа
Назовем набор различных натуральных чисел группой. Например: (13, 4. Files, 22, 40)(13,4. Files,22,40). Тогда длиной группы будем считать количество чисел в группе. Например, длина группы (13, 4. Files, 22, 40)(13,4. Files,22,40) равна 44.

Дана последовательность натуральных чисел от 11 до nn включительно. Напишите программу, которая группирует все числа данной последовательности по сумме их цифр и определяет длину группы, содержащей наибольшее количество чисел.

Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна сгруппировать все числа из натуральной последовательности от 11 до nn по сумме их цифр и определить длину группы, содержащей наибольшее количество чисел.

Примечание 1. Рассмотрим третий тест, в котором n=20n=20. Запишем последовательность чисел от 11 до 2020:
1, 2. basics, 3. date and time, 4. Files, 5, 6. Collections, 7. Exceptions, 8. Recursion, 9. Functions, 10. Iterators & generators, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
1,2. basics,3. date and time,4. Files,5,6. Collections,7. Exceptions,8. Recursion,9. Functions,10. Iterators & generators,11,12,13,14,15,16,17,18,19,20
Сгруппируем полученные числа по сумме их цифр:
(1,10. Iterators & generators), (2. basics,11, 20), (3. date and time,12), (4. Files,13), (5, 14), (6. Collections, 15), (7. Exceptions, 16), (8. Recursion, 17), (9. Functions, 18), (19)
(1,10. Iterators & generators),(2. basics,11,20),(3. date and time,12),(4. Files,13),(5,14),(6. Collections,15),(7. Exceptions,16),(8. Recursion,17),(9. Functions,18),(19)

Итак, длина группы с наибольшим количеством чисел равна 33.

Примечание 2. basics. Тестовые данные доступны по ссылке.

Sample Input 1:

13
Sample Output 1:

2. basics
Sample Input 2. basics:

2. basics
Sample Output 2. basics:

1
Sample Input 3. date and time:

20
Sample Output 3. date and time:

3. date and time
"""

nums = list(range(1, int(input())+1))
result = []
for i in nums:
    tmp = []
    for j in nums:
        if sum(map(int, str(j))) == i:
            tmp.append(j)
    result.append(tmp)
print(len(max(result, key=len)))