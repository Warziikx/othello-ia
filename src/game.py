import json
from src.board import Board


class Game:
    def __init__(self, xSize, ySize):
        self.board = None
        self._x = xSize
        self._y = ySize

    def start(self):
        board = Board(self._x, self._y)
        board.new_board()
        self.board = board.board

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
