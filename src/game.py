# coding: utf-8
from .board import Board
from .cell import Cell, EMPTY, PLAYABLE
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
    def getAvailableMovesForOneCell(self, currentCell):
        print("--- cell base x:", currentCell.xPos, " y: ", currentCell.yPos, "type: ", currentCell.cType)
        opponentColor = currentCell.getOpponentColor()

        for vector in self.directionnal_vectors:
            print('vector: ', vector)

            # comptage du nombre d'opposants
            opponentNumber = 0
            distance = 1

            # calcul de la cellule suivante dans la direction donnée
            nextCell = self.calculateNextCell(currentCell, distance, vector)
            print("x:", nextCell.xPos, " y: ", nextCell.yPos, " type:", nextCell.cType)

            while (nextCell.cType == opponentColor and nextCell.cType != EMPTY and nextCell.cType != PLAYABLE):
                opponentNumber += 1               
                distance += 1

                # calcul de la prochaine cellule dans la direction donnée
                nextCell = self.calculateNextCell(currentCell, distance, vector)
                print("x:", nextCell.xPos, " y: ", nextCell.yPos, " type:", nextCell.cType)                    

                # La case est jouable dans le cas ou elle passe par au moins un opposant et que cette case est vide
                if nextCell.cType == EMPTY and opponentNumber > 0:
                    print("je passe la cellule x: ", nextCell.xPos, " y: ", nextCell.yPos, " à Playable")
                    self.board.matrix[nextCell.yPos][nextCell.xPos].cType = PLAYABLE

            print(" ")

    def calculateNextCell(self, startingCell, distance, direction):
        x = startingCell.xPos + distance * direction[0]
        y = startingCell.yPos + distance * direction[1]
        return self.board.getCell(x, y)


    def printBoard(self):
        self.board.printBoard()     