"""
https://stepik.org/lesson/864077/step/8?unit=923013

Классы Testpaper и Student
В этой задаче вам необходимо реализовать класс Testpaper, который позволит составлять экзаменационные тесты. Каждый тест должен создаваться на основе темы, схемы верных ответов и минимального процента верных решений:

testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
Созданные тесты должны сдаваться студентом — экземпляром класса Student. Он должен иметь метод take_test(), который принимает в качестве аргументов тест и ответы студента на этот тест:

student1 = Student()
student2 = Student()

student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
Результаты тестов должны быть доступны в виде словаря, ключом в котором является тема теста, а значением — результат теста (сдан или не сдан), а также процент верных решений:

print(student1.tests_taken)    # {'Maths': 'Passed! (80%)'}
print(student2.tests_taken)    # {'Chemistry': 'Failed! (25%)', 'Computing': 'Failed! (43%)'}
Если студент еще не сдал ни одного теста, атрибут tests_taken должен содержать строку No tests taken:

student3 = Student()

print(student3.tests_taken)    # No tests taken
Примечание 1. Округление процента верных решений должно происходить до ближайшего целого числа.
"""

class Testpaper:

    def __init__(self):
        self.tests_taken = 'No tests taken'

    def __init__(self, subj, answ, grade):
        self.subj = subj
        self.answ = answ
        self.grade = grade

class Student:

    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, test, answer):

        pas = 'Passed! '
        result = f'{round(len(set(test.answ).intersection(set(answer)))/len(answer) * 100)}%'

        if not isinstance(self.tests_taken, dict):
            self.tests_taken = {}

        if result < test.grade:
            pas = 'Failed! '

        self.tests_taken[test.subj] = pas + f'({result})'

        return result
