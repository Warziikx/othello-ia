from .board import Board
from .cell import BLACK, WHITE, EMPTY, PLAYABLE
from itertools import product
import operator

class Game:
    def __init__(self, size):
        self.size = size
        self.board = Board(self.size)
        self.board.initBoard()
        # self.directionnal_vectors = product((-1, 0, 1), (-1, 0, 1))
        # self.directionnal_vectors = (vectors for vectors in self.directionnal_vectors if not vectors == (0, 0))
        self.directionnal_vectors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    # get available moves depending of player (White, Black)
    def getAvailableMoves(self, playerType):
        # parcours du plateau en entier
        for x in range(self.size):
            for y in range(self.size):
                if self.board.matrix[x][y].cType == playerType:
                    self.getAvailableMovesForOneCell(self.board.matrix[x][y])
        return self.board.matrix
    
    # get moves per cell
    def getAvailableMovesForOneCell(self, myCell):
        print("cell base x:", myCell.xPos, " y: ", myCell.yPos, "type: ", myCell.cType)
        opponentColor = myCell.getOpponentColor()

        for vector in self.directionnal_vectors:
            print('vector: ', vector)
            try:
                distance = 1
                xNextCell = myCell.xPos + distance * vector[1]
                yNextCell = myCell.yPos + distance * vector[0]
                nextCell = self.board.getCell(xNextCell, yNextCell)
                print("x1:", xNextCell, " y1: ", yNextCell, "type: ", nextCell.cType)
                
                while (nextCell.cType == opponentColor and nextCell.cType != EMPTY and nextCell.cType != PLAYABLE):
                    try:
                        distance += 1
                        xNextCell = cell.xPos + distance * vector[1]
                        yNextCell = cell.yPos + distance * vector[0]
                        nextCell = self.board.getCell(xNextCell, yNextCell)

                        print("x:", xNextCell, " y: ", yNextCell, " type:", nextCell.cType)
                    except:
                        print("Out of bound 1, distance: ", distance)
                        break
            except:
                print("Out of bound 2")
                continue 

            if nextCell.cType == EMPTY:
                self.board.matrix[nextCell.xPos][nextCell.yPos].cType = PLAYABLE
                print(" ")  

    def printBoard(self):
        self.board.printBoard()     