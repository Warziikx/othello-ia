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
        return self.cType

