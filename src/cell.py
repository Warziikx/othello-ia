EMPTY = "empty"
WHITE = "white"
BLACK = "black"
class Cell:

    def __init__(self):
        pass

    def new_cell(self, xPos, yPos, cType=EMPTY):
        return {'x': xPos, 'y': yPos, 'type': cType}


    def get_symbol(self, cell):
        """ Return cell symbol from cell type """

        if cell['type'] == self.BLACK:
            return "○"
        if cell['type'] == self.WHITE:
            return "●"

        return " "


    def get_types(self):
        return {self.WHITE, self.BLACK, self.EMPTY}


    def extract_positions(self, cells):
        return list(map(lambda cell: (cell['x'], cell['y']), cells))