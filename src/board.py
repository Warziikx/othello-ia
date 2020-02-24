import copy

from .cell import Cell, EMPTY, WHITE, BLACK, PLAYABLE

dirx = [-1, 0, 1, -1, 1, -1, 0, 1]
diry = [-1, -1, -1, 0, 0, 1, 1, 1]


class Board:
    def __init__(self, size, board=None, *args, **kwargs):
        if board is None:
            board = []
        self.size = int(size)
        self.board = board
        if len(board) > 0:
            for x in range(self.size):
                for y in range(self.size):
                    if type(self.board[x][y]) is not Cell:
                        self.board[x][y] = Cell(**self.board[x][y])

    def is_even(self, x):
        return x % 2 == 0

    def new_board(self):
        self.board = []
        if not self.is_even(self.size) or not self.is_even(self.size):
            raise ValueError("Board x/y size must be even.")
        if self.size < 4 or self.size < 4:
            raise ValueError("Board must have 4 rows or columns at least")
        # self.board
        for x in range(self.size):
            self.board.append([])
            for y in range(self.size):
                self.board[x].append(Cell(x, y))
        departure_pos = self.get_departure_cells(self.board)
        self.board[departure_pos[0].x][departure_pos[0].y] = departure_pos[0]
        self.board[departure_pos[1].x][departure_pos[1].y] = departure_pos[1]
        self.board[departure_pos[2].x][departure_pos[2].y] = departure_pos[2]
        self.board[departure_pos[3].x][departure_pos[3].y] = departure_pos[3]
        for x in range(self.size):
            for y in range(self.size):
                self.board[x][y] = Cell(x, y, PLAYABLE) if self.is_valid_move(x, y, WHITE) else self.board[x][y]

    def get_departure_cells(self, matrix):
        x_middle = int(self.size / 2)
        y_middle = int(self.size / 2)
        return [
            Cell(x_middle, y_middle, BLACK),
            Cell(x_middle - 1, y_middle - 1, BLACK),
            Cell(x_middle - 1, y_middle, WHITE),
            Cell(x_middle, y_middle - 1, WHITE)
        ]

    def is_valid_move(self, x, y, player):
        if x < 0 or x > self.size - 1 or y < 0 or y > self.size - 1:
            return False
        if self.board[x][y].type != EMPTY and self.board[x][y].type != PLAYABLE:
            return False
        temp_board = copy.deepcopy(self)
        totctr = temp_board.make_move(x, y, player)
        if totctr == 0:
            return False
        return True

    def eval(self, player):
        value = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == player:
                    if (x == 0 or x == self.size - 1) and (y == 0 or y == self.size - 1):
                        value += 4  # Coin
                    elif (x == 0 or x == self.size - 1) or (y == 0 or y == self.size - 1):
                        value += 2  # coté
                    else:
                        value += 1
        return value

    def make_move(self, x, y, player):  # assuming valid move
        totctr = 0  # total number of opponent pieces taken
        self.board[x][y] = Cell(x, y, player)
        for d in range(8):  # 8 directions
            ctr = 0
            for i in range(self.size):
                dx = x + dirx[d] * (i + 1)
                dy = y + diry[d] * (i + 1)
                if dx < 0 or dx > self.size - 1 or dy < 0 or dy > self.size - 1:
                    ctr = 0
                    break
                elif self.board[dx][dy].type == player:
                    break
                elif self.board[dx][dy].type == EMPTY:
                    ctr = 0
                    break
                elif self.board[dx][dy].type == PLAYABLE:
                    ctr = 0
                    break
                else:
                    ctr += 1
            for i in range(ctr):
                dx = x + dirx[d] * (i + 1)
                dy = y + diry[d] * (i + 1)
                self.board[dx][dy] = Cell(dy, dx, player)
            totctr += ctr
        return totctr

    def is_terminal(self, player):
        for x in range(self.size):
            for y in range(self.size):
                if self.is_valid_move(x, y, player):
                    return False
        return True

    def get_playable(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y].type == PLAYABLE:
                    self.board[x][y] = Cell(x, y, EMPTY)
        for x in range(self.size):
            for y in range(self.size):
                if self.is_valid_move(x, y, WHITE):
                    self.board[x][y] = Cell(x, y, PLAYABLE) if self.is_valid_move(x, y, WHITE) else self.board[x][y]
