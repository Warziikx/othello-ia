from .matrix import Matrix
from .cell import Cell, EMPTY, WHITE, BLACK

class Board:
    def __init__(self):
        pass

    def is_even(self, x):
        return x % 2 == 0
    def new_board(self, xSize, ySize):
        if not self.is_even(xSize) or not self.is_even(ySize):
            raise ValueError("Board x/y size must be even.")
        if ySize < 4 or xSize < 4:
            raise ValueError("Board must have 4 rows or columns at least")
        matrix = Matrix()
        return matrix.new_matrix(xSize, ySize)
    
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
