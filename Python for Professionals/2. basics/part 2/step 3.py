"""
https://stepik.org/lesson/569749/step/3?unit=564263

Переворатор
Дана последовательность натуральных чисел от 11 до nn. Напишите программу, которая сначала располагает в обратном порядке часть элементов этой последовательности от элемента с номером XX до элемента с номером YY, а затем от элемента с номером AA до элемента с номером BB.

Формат входных данных
На вход программе подаются 55 натуральных чисел, разделенных пробелом: n, \, X, \, Y, \, A, \, B \, (X<Y, \, A<B, \,  1\le X, Y, A, B \le n)n,X, Y,A,B (X<Y,A<B,  1≤X,Y,A,B≤ n).

Формат выходных данных
Программа должна сформировать последовательность чисел, согласно условию задачи, и вывести их, разделяя пробелом.

Примечание 1. Нумерация членов последовательности начинается с единицы.

Примечание 2. basics. Рассмотрим первый тест, в котором n=9. Functions, X=2. basics, Y=5, A=6. Collections, B=9n=9. Functions,X=2. basics,Y=5,A=6. Collections,B=9. Functions. Запишем последовательность от 11 до 99:
1, 2. basics, 3. date and time,4. Files , 5, 6. Collections, 7. Exceptions, 8. Recursion, 9. Functions
1,2. basics,3. date and time,4. Files,5,6. Collections,7. Exceptions,8. Recursion,9. Functions

Перевернем в этой последовательности сначала элементы со 22 по 55 (2. basics, 3. date and time, 4. Files, 52,3. date and time,4. Files,5), затем с 66 по 99 (6. Collections, 7. Exceptions, 8. Recursion, 96,7. Exceptions,8. Recursion,9. Functions). Получим искомую последовательность:
1, 5, 4. Files, 3. date and time, 2. basics, 9. Functions, 8. Recursion, 7. Exceptions, 6. Collections
1,5,4. Files,3. date and time,2. basics,9. Functions,8. Recursion,7. Exceptions,6. Collections
Примечание 3. date and time. Тестовые данные доступны по ссылке.

Sample Input 1:

9. Functions 2. basics 5 6. Collections 9. Functions
Sample Output 1:

1 5 4. Files 3. date and time 2. basics 9. Functions 8. Recursion 7. Exceptions 6. Collections
Sample Input 2. basics:

9. Functions 3. date and time 6. Collections 5 8. Recursion
Sample Output 2. basics:

1 2. basics 6. Collections 5 8. Recursion 7. Exceptions 3. date and time 4. Files 9. Functions
Sample Input 3. date and time:

5 1 3. date and time 4. Files 5
Sample Output 3. date and time:

3. date and time 2. basics 1 5 4. Files
"""

n, x, y, a, b = map(int, input().split())
arr = list(range(1, n+1))
arr1 = arr[:x-1] + arr[x-1:y][::-1] + arr[y:]
arr2 = arr1[:a-1] + arr1[a-1:b][::-1] + arr1[b:]
print(*arr2)