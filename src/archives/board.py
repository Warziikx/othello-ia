from .matrix import Matrix
from .cell import Cell, EMPTY, WHITE, BLACK
from .vector import Vector


class Board:

    def __init__(self, xSize, ySize):
        self.matrix = Matrix()
        self.vector = Vector()
        self.cell = Cell()
        self.board = []
        self.xSize = xSize
        self.ySize = ySize

    def is_even(self, x):
        return x % 2 == 0

    def new_board(self):
        if not self.is_even(self.xSize) or not self.is_even(self.ySize):
            raise ValueError("Board x/y size must be even.")
        if self.ySize < 4 or self.xSize < 4:
            raise ValueError("Board must have 4 rows or columns at least")
        self.board = self.matrix.new_matrix(self.xSize, self.ySize)
        departure_pos = self.get_departure_cells(self.board)
        self.board[departure_pos[0]['x']][departure_pos[0]['y']] = departure_pos[0]['type']
        self.board[departure_pos[1]['x']][departure_pos[1]['y']] = departure_pos[1]['type']
        self.board[departure_pos[2]['x']][departure_pos[2]['y']] = departure_pos[2]['type']
        self.board[departure_pos[3]['x']][departure_pos[3]['y']] = departure_pos[3]['type']

    def get_departure_cells(self, matrix):
        xSize, ySize = self.matrix.get_size(matrix)
        x_middle = int(xSize / 2)
        y_middle = int(ySize / 2)
        return [
            self.cell.new_cell(x_middle, y_middle, BLACK),
            self.cell.new_cell(x_middle - 1, y_middle - 1, BLACK),
            self.cell.new_cell(x_middle - 1, y_middle, WHITE),
            self.cell.new_cell(x_middle, y_middle - 1, WHITE)
        ]

    def get_flipped_cells_from_cell_change(self, cell):
        flipped_cells = []
        empty_cell = self.cell.new_cell(0, 0, EMPTY)
        xPos, yPos, cType = cell['x'], cell['y'], cell['type']
        if not self.matrix.get_cell(self.board, xPos, yPos, empty_cell)['type'] is EMPTY:
            return []

        # Loop over all possibles directions (except null vector)
        for vector in self.vector.get_directionnal_vectors():
            vector_add_generator = self.vector.get_vector_add_generator((xPos, yPos), vector)
            vector_flipped_cells = []

            # While there's no empty cell, same color disk or border, go forward
            for (x, y) in vector_add_generator:
                if self.matrix.get_cell(self.board, x, y, empty_cell)['type'] in [EMPTY, cType]:
                    break
                vector_flipped_cells.append(c.new_cell(x, y, cType))

            # If the're flipped disks and last cell has same type, it's ok
            last_cell = self.matrix.get_cell(self.board, x, y, empty_cell)
            if len(vector_flipped_cells) > 0 and last_cell['type'] is cType:
                flipped_cells += vector_flipped_cells

        return flipped_cells

    def is_legal_cell_change(self, cell):
        return len(self.get_flipped_cells_from_cell_change(cell)) > 0

    def get_legal_cell_changes(self):
        """ Return legal cell changes for each types """

        legal_cell_changes = {WHITE: [], BLACK: []}
        cell = Cell()
        for cType in [WHITE, BLACK]:
            for row_idx, row in enumerate(self.board):
                for col_idx, col in enumerate(row):
                    cell_change = cell.new_cell(col_idx, row_idx, cType)
                    if self.is_legal_cell_change(cell_change):
                        legal_cell_changes[cType].append(cell_change)

        return legal_cell_changes
