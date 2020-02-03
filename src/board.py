from .cell import Cell, EMPTY, WHITE, BLACK
class Board:
    def __init__(self, size):
        self.size = size
        # self.matrix = [[]]
        self.matrix = [[Cell(x,y, EMPTY) for x in range(self.size)] for y in range(self.size)]
        # for x in range(self.size -1):
        #     for y in range(self.size -1):
        #         self.matrix[x][y] = Cell(x, y, EMPTY)
        # print(self.matrix)
        print(self.matrix)

    def initBoard(self):
        if not self.size %2 == 0:
            raise ValueError("La taille du plateau doit être un multiple de 2.")
        if self.size < 4:
            raise ValueError("Le plateau est trop petit !")
        x_middle = int(self.size / 2)
        y_middle = int(self.size / 2)
        self.matrix[x_middle][y_middle] = Cell(x_middle, y_middle ,BLACK)
        self.matrix[x_middle - 1][y_middle - 1] = Cell(x_middle - 1, y_middle - 1,BLACK)
        self.matrix[x_middle - 1][y_middle] = Cell(x_middle - 1, y_middle ,WHITE)
        self.matrix[x_middle][y_middle - 1] = Cell(x_middle, y_middle - 1 ,WHITE)

    # def getPlayableCells(self, cell):
