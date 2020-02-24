import copy

dirx = [-1, 0, 1, -1, 1, -1, 0, 1]
diry = [-1, -1, -1, 0, 0, 1, 1, 1]


class MinMax:

    def __init__(self, game):
        self.game = game
        self.min_eval_board = -1  # min - 1
        self.max_eval_board = self.game.size * self.game.size + 4 * self.game.size + 4 + 1  # max + 1

    def best_move(self, player):
        maxPoints = 0
        mx = -1
        my = -1
        for x in range(self.game.size):
            for y in range(self.game.size):
                board_temp = copy.deepcopy(self.game.board)
                if board_temp.is_valid_move(x, y, player):
                    totctr = board_temp.make_move(x, y, player)
                    points = self.alpha_beta(board_temp, player, self.game.depth, self.min_eval_board, self.max_eval_board,
                                            True)
                    if points > maxPoints:
                        maxPoints = points
                        mx = x
                        my = y
        return (mx, my)

    def alpha_beta(self, board, player, depth, alpha, beta, maximizing_payer):
        if depth == 0 or board.is_terminal(player):
            return board.eval(player)
        v = self.max_eval_board if maximizing_payer else self.min_eval_board
        for x in range(self.game.size):
            for y in range(self.game.size):
                if board.is_valid_move(x, y, player):
                    board_temp = copy.deepcopy(board)
                    totctr = board_temp.make_move(x, y, player)
                    alpha_beta_return = self.alpha_beta(board_temp, player, depth - 1, alpha, beta, not maximizing_payer)
                    alpha_beta_return = int(alpha_beta_return)
                    v = max(v, alpha_beta_return) if maximizing_payer else min(v, alpha_beta_return)
                    if maximizing_payer:
                        alpha = max(alpha, v)
                    else:
                        beta = min(beta, v)
                    if beta <= alpha:
                        break
        return v
