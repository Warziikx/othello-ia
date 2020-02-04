import copy

dirx = [-1, 0, 1, -1, 1, -1, 0, 1]
diry = [-1, -1, -1, 0, 0, 1, 1, 1]


class MinMax:

    def __init__(self, game):
        self.game = game
        self.minEvalBoard = -1  # min - 1
        self.maxEvalBoard = self.game.size * self.game.size + 4 * self.game.size + 4 + 1  # max + 1

    def best_move(self, player):
        maxPoints = 0
        mx = -1
        my = -1
        for x in range(self.game.size):
            for y in range(self.game.size):
                boardTemp = copy.deepcopy(self.game.board)
                if boardTemp.is_valid_move(x, y, player):
                    totctr = boardTemp.make_move(x, y, player)
                    points = self.AlphaBeta(boardTemp, player, self.game.depth, self.minEvalBoard, self.maxEvalBoard,
                                            True)
                    if points > maxPoints:
                        maxPoints = points
                        mx = x
                        my = y
        return (mx, my)

    def AlphaBeta(self, board, player, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or board.is_terminal(player):
            return board.eval(player)
        v = self.maxEvalBoard if maximizingPlayer else self.minEvalBoard
        for x in range(self.game.size):
            for y in range(self.game.size):
                boardTemp = copy.deepcopy(board)
                if boardTemp.is_valid_move(x, y, player):
                    totctr = boardTemp.make_move(x, y, player)
                    alpha_beta_return = self.AlphaBeta(boardTemp, player, depth - 1, alpha, beta, not maximizingPlayer)
                    alpha_beta_return = int(alpha_beta_return)
                    v = max(v, alpha_beta_return) if maximizingPlayer else min(v, alpha_beta_return)
                    if maximizingPlayer:
                        alpha = max(alpha, v)
                    else:
                        beta = min(beta, v)
                    if beta <= alpha:
                        break
        return v
