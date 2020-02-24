import copy
import json
from src.board import Board


class Game:
    def __init__(self, size, board, depth, *args, **kwargs):
        self.board = board
        self.size = size
        self.depth = depth
        # self.min_eval_board = -1  # min - 1
        # self.max_eval_board = self.x * self.x + 4 * self.x + 4 + 1  # max + 1

    def start(self):
        board = Board(self.size)
        board.new_board()
        self.board = board
        print(self.board)

    def toJSON(self):
        data = json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
        return data
