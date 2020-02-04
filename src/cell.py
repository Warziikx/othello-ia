import copy

EMPTY = "empty"
WHITE = "white"
BLACK = "black"
PLAYABLE = "playable"


class Cell:

    def __init__(self, x, y, type=EMPTY, *args, **kwargs):
        self.x = x
        self.y = y
        self.type = type
        pass

    def new_cell(self, xPos, yPos, cType=EMPTY):
        return {'x': xPos, 'y': yPos, 'type': cType}

    def get_symbol(self, cell):
        """ Return cell symbol from cell type """

        if cell['type'] == BLACK:
            return "○"
        if cell['type'] == WHITE:
            return "●"

        return " "

    def get_types(self):
        return {WHITE, BLACK, EMPTY}

    def extract_positions(self, cells):
        return list(map(lambda cell: (cell['x'], cell['y']), cells))

    def is_terminal(self, board, player):
        for y in range(self.x):
            for x in range(self.x):
                if self.ValidMove(board, x, y, player):
                    return False
        return True
