"""
https://stepik.org/lesson/864077/step/10?unit=923013

Классы Game и Cell
В этой задаче вам необходимо реализовать поле для игры в Сапера в виде двух классов Game и Cell. Экземпляр первого класса будет описывать само игровое поле, экземпляр класса Cell — одну его ячейку. Экземпляр класса Game должен создаваться на основе трех значений: количество строк (длина поля), количество столбцов (ширина поля) и общее количество мин на поле:

game = Game(14, 18, 40)    # 14 строк, 18 столбцов и 40 мин
Количество строк и столбцов, а также общее количество мин должны быть доступны по соответствующим атрибутам:

print(game.rows)           # 14
print(game.cols)           # 18
print(game.mines)          # 40
Также экземпляр класса Game должен иметь атрибут board, представляющий игровое поле в виде двумерного списка. Количество подсписков в этом списке должно совпадать с количеством строк, количество элементов в подсписках — с количеством столбцов. Каждый элемент подсписка должен представлять собой экземпляр класса Cell и иметь соответствующий набор атрибутов:

cell = game.board[0][0]

print(cell.row)            # 0; строка ячейки
print(cell.col)            # 0; столбец ячейки
print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
print(cell.open)           # True или False в зависимости от того, открыта ячейка или нет, по умолчанию закрыта
print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках
Игровое поле при создании должно заполняться минами случайным образом.

Примечание 1. Для проверки того, что в экземпляре класса Cell хранится верное количество мин в соседних ячейках, в одном из тестов мы используем собственную функцию get_neighbours_count(), которая считает это количество.
"""

from random import randint

class Game:

    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.mines_count = 0
        self.board = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.fill_with_mines()
        self.count_neighbours()

    def fill_with_mines(self):
        while self.mines_count < self.mines:
            r = randint(0, self.rows-1)
            c = randint(0, self.cols-1)
            if not self.board[r][c].mine:
                self.board[r][c].mine = True
                self.mines_count += 1


    def count_neighbours(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.board[i][j]
                if not cell.mine:
                    mines = 0
                    for row in [-1, 0, 1]:
                        row += i
                        for col in [-1, 0, 1]:
                            col += j
                            if row in range(self.rows) and col in range(self.cols):
                                neighbour = self.board[row][col]
                                if neighbour.mine:
                                    mines += 1
                    cell.neighbours = mines

class Cell:

    def __init__(self, row, col, mine=False):
        self.row = row
        self.col = col
        self.mine = mine
        self.open = False
        self.neighbours = 0
    def __repr__(self):
        return f'{self.row, self.col, self.mine}'
