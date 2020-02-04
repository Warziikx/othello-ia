# coding: utf-8
from .cell import Cell, EMPTY, WHITE, BLACK

class Board:
    def __init__(self, size):
        self.size = size
        # self.matrix = [[]]
        self.matrix = [[Cell(x,y, EMPTY) for x in range(self.size)] for y in range(self.size)]
        self.printBoard()

    def initBoard(self):
        if not self.size %2 == 0:
            raise ValueError("La taille du plateau doit être un multiple de 2.")
        if self.size < 4:
            raise ValueError("Le plateau est trop petit !")
        x_middle = int(self.size / 2)
        y_middle = int(self.size / 2)
        self.matrix[x_middle][y_middle] = Cell(x_middle, y_middle, BLACK)
        self.matrix[x_middle - 1][y_middle - 1] = Cell(x_middle - 1, y_middle - 1, BLACK)
        self.matrix[x_middle - 1][y_middle] = Cell(x_middle - 1, y_middle, WHITE)
        self.matrix[x_middle][y_middle - 1] = Cell(x_middle, y_middle - 1, WHITE)
        self.printBoard()

    # Print board in console
    def printBoard(self):
        print(" ")
        for x in range(self.size):
            for y in range(self.size):
                print(self.matrix[x][y].toString(), end=" ")
            print(" ")
        print(" ")

    def getCell(self, x, y):
        return self.matrix[x][y] ? self.matrix[x][y] : None
        
