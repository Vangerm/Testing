import random as r


class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False) -> None:
        self.around_mines: int = around_mines
        self.mine: bool = mine
        self.fl_open: bool = False


class GamePole:
    def init(self, N: int, M: int) -> None:
        self.cord_mines: list[tuple] = []   # координаты мин
        self.N: int = N
        self.pole: list[list] = [[Cell() for _ in range(N)] for _ in range(N)]
        for i in range(M):
            x, y = self.plant_mine()    # установка мин по полю
            self.pole[x][y].mine = True
        self.check_mines()  # установка значений вокруг мин

    def plant_mine(self) -> tuple:
        'метод для закладки мин по полю'
        while True:
            x = r.randint(0, self.N - 1)
            y = r.randint(0, self.N - 1)
            if (x, y) not in self.cord_mines:
                break
        self.cord_mines.append((x, y))
        return (x, y)

    def check_mines(self) -> None:
        'метод расстановки чисел в кол-ве находящихся рядом мин'
        for line in range(self.N):
            for column in range(self.N):
                if self.pole[line][column].mine:
                    continue
                cord = [-1, 0, 1]
                if line - 1 >= 0 and line + 1 <= self.N-1 and \
                        column - 1 >= 0 and column + 1 <= self.N-1:
                    self.pole[line][column].around_mines = \
                        self.check_lines(column, line, cord, cord)
                elif not line and not column:   # 0;0
                    self.pole[line][column].around_mines = \
                        self.check_lines(column, line, cord[1:], cord[1:])
                elif not line and column == self.N - 1:     # N;0
                    self.pole[line][column].around_mines = \
                        self.check_lines(column, line, cord[:-1], cord[1:])
                elif line == self.N - 1 and not column:     # 0;N
                    self.pole[line][column].around_mines = \
                        self.check_lines(column, line, cord[1:], cord[:-1])
                elif line == self.N - 1 and column == self.N - 1:   # N;N
                    self.pole[line][column].around_mines = \
                        self.check_lines(column, line, cord[:-1], cord[:-1])
                elif line - 1 < 0:
                    self.pole[line][column].around_mines = \
                        self.check_lines(column, line, cord, cord[1:])
                elif line + 1 > self.N - 1:
                    self.pole[line][column].around_mines = \
                        self.check_lines(column, line, cord, cord[:-1])
                elif column - 1 < 0:
                    self.pole[line][column].around_mines = \
                        self.check_lines(column, line, cord[1:], cord)
                elif column + 1 > self.N - 1:
                    self.pole[line][column].around_mines = \
                        self.check_lines(column, line, cord[:-1], cord)

    def check_lines(self, column, line, x_cord: list, y_cord: list) -> int:
        'метод проверки вокруг клетки (ячейки)'
        count = 0
        for j in x_cord:
            for i in y_cord:
                if not x_cord and not y_cord:
                    continue
                if self.pole[line + i][column + j].mine:
                    count += 1
        return count

    def show(self):
        'метод представления поля'
        for line in range(self.N):
            for column in range(self.N):
                if not self.pole[line][column].fl_open:
                    print('#', end=' ')
                elif self.pole[line][column].mine:
                    print('*', end=' ')
                else:
                    print(self.pole[line][column].around_mines, end=' ')
            print()


pole_game = GamePole()
pole_game.init(10, 12)
