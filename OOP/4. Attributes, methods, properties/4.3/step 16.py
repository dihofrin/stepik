"""
https://stepik.org/lesson/794582/step/16?unit=797335

Класс Knight ♞

Реализуйте класс Knight, описывающий шахматного коня.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:

horizontal — координата коня по горизонтали, представленная латинской буквой от a до h
vertical — координата коня по вертикали, представленная целым числом от 1 до 8 включительно
color — цвет коня (black или white)


Экземпляр класса Knight должен иметь три атрибута:

horizontal — координата коня на шахматной доске по горизонтали
vertical — координата коня на шахматной доске по вертикали
color — цвет коня


Класс Knight должен иметь четыре метода экземпляра:

get_char() — метод, возвращающий символ N
can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали, и возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали и заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с указанными координатами, его координаты должны остаться неизменными
draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь, — символом *
"""

class Knight:

    cells = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    def __init__(self, horizontal, vertical, color):
        self.horizontal = ord(horizontal) - 94
        self.vertical = int(vertical)-1
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, horizontal, vertical):
        return abs(self.horizontal - horizontal) * abs(self.vertical - vertical) == 2

    def move_to(self, horizontal, vertical):
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self):
        board = [['.'] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if self.can_move(i, j):
                    board[i][j] = '*'
                if i == self.horizontal and j == self.vertical:
                        board[i][j] = self.get_char()
        for row in board:
            print(*row, sep='')


knight = Knight('c', 3, 'white')

print(knight.color, knight.get_char())
print(knight.horizontal, knight.vertical)