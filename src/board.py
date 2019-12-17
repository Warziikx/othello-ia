from .matrix import Matrix

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