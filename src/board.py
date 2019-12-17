from .matrix import Matrix
from .cell import Cell, EMPTY, WHITE, BLACK

class Board:
    board = []
    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize

    def is_even(self, x):
        return x % 2 == 0
    def new_board(self):
        if not self.is_even(self.xSize) or not self.is_even(self.ySize):
            raise ValueError("Board x/y size must be even.")
        if self.ySize < 4 or self.xSize < 4:
            raise ValueError("Board must have 4 rows or columns at least")
        matrix = Matrix()
        self.board =  matrix.new_matrix(self.xSize, self.ySize)
        departure_pos = self.get_departure_cells(self.board)
        self.board[departure_pos[0]['x']][departure_pos[0]['y']] = departure_pos[0]['type']
        self.board[departure_pos[1]['x']][departure_pos[1]['y']] = departure_pos[1]['type']
        self.board[departure_pos[2]['x']][departure_pos[2]['y']] = departure_pos[2]['type']
        self.board[departure_pos[3]['x']][departure_pos[3]['y']] = departure_pos[3]['type']


    def get_departure_cells(self, matrix):
        m = Matrix()
        xSize, ySize = m.get_size(matrix)

        x_middle = int(xSize/2)
        y_middle = int(ySize/2)
        cell = Cell()
        return [
            cell.new_cell(x_middle, y_middle, BLACK),
            cell.new_cell(x_middle - 1, y_middle - 1, BLACK),
            cell.new_cell(x_middle - 1, y_middle, WHITE),
            cell.new_cell(x_middle, y_middle - 1, WHITE)
        ]
