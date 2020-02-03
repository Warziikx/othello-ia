# coding: utf-8
EMPTY = "empty"
WHITE = "white"
BLACK = "black"
PLAYABLE = "playable"

class Cell:
    def __init__(self, xPos, yPos, cType = EMPTY):
        self.xPos = xPos
        self.yPos = yPos
        self.cType = cType

    def toString(self):
        if self.cType == WHITE:
            return "b"
        elif self.cType == BLACK:
            return "n"
        elif self.cType == EMPTY:
            return "-"
        else:
            return "j"

    def getOpponentColor(self):
        if (self.cType == WHITE):
            return BLACK
        elif (self.cType == BLACK):
            return WHITE
        else:
            raise ValueError("Les cellules Vide ou Jouable n'ont pas d'opposé")

