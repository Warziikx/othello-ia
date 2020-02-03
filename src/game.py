import json
from src.board import Board


class Game:
    def __init__(self, x, y, board, *args, **kwargs):
        self.board = board
        self.x = x
        self.y = y

    def start(self):
        board = Board(self.x, self.y)
        board.new_board()
        self.board = board.board

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
