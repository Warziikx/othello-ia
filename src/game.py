from .board import Board

class Game:
    def __init__(self, size):
        self.size = size
        self.board = Board(self.size)
        self.board.initBoard()
    