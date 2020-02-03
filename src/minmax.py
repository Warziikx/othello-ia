# n est la taille du tableau
minEvalBoard = -1  # min - 1
maxEvalBoard = n * n + 4 * n + 4 + 1  # max + 1


# Boucle récursive alpha beta
# Si il ne s'agis pas niveau de profondeur max ou qu'il est encore possible de jouer
# On retourne l'évaluation du board

# Si on est dans le cas de max(C'est le tour de l'ia)
# On boucle sur y
# On boucle sur x
# Si l'on peut jouer sur ces coordonnée
# On fait le move sur une copy du board

# Sinon c'est le cas de min (tour du joueur)
# On boucle sur y
# On boucle sur x
# Si l'on peut jouer sur ces coordonnée
# On fait le move sur une copy du board

# Evalue la situation du board
def EvalBoard(board, player):
    value = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == player:
                if (x == 0 or x == n - 1) and (y == 0 or y == n - 1):
                    tot += 4  # Coin
                elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1):
                    tot += 2  # coté
                else:
                    tot += 1
    return tot


def AlphaBeta(board, player, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or IsTerminalNode(board, player):
        return EvalBoard(board, player)
    v = minEvalBoard if maximizingPlayer else maxEvalBoard
    for y in range(n):
        for x in range(n):
            if ValidMove(board, x, y, player):
                (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                alpha_beta_return = AlphaBeta(boardTemp, player, depth - 1, alpha, beta, not maximizingPlayer)
                v = max(v, alpha_beta_return) if maximizingPlayer else min(v, alpha_beta_return)
                if maximizingPlayer:
                    alpha = max(alpha, v)
                else:
                    beta = min(beta, v)

                if beta <= alpha:
                    break

    def BestMove(board, player):
        maxPoints = 0
        mx = -1
        my = -1
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    points = AlphaBeta(board, player, depth, minEvalBoard, maxEvalBoard, True)
                    if points > maxPoints:
                        maxPoints = points
                        mx = x
                        my = y
        return (mx, my)

    # if maximizingPlayer:
    #     v = minEvalBoard
    #     for y in range(n):
    #         for x in range(n):
    #             if ValidMove(board, x, y, player):
    #                 (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
    #                 v = max(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, False))
    #                 alpha = max(alpha, v)
    #                 if beta <= alpha:
    #                     break  # beta cut-off
    #     return v
    # else:  # minimizingPlayer
    #     v = maxEvalBoard
    #     for y in range(n):
    #         for x in range(n):
    #             if ValidMove(board, x, y, player):
    #                 (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
    #                 v = min(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, True))
    #                 beta = min(beta, v)
    #                 if beta <= alpha:
    #                     break  # alpha cut-off
    #     return v

# def AlphaBeta(board, player, depth, alpha, beta, maximizingPlayer):
#     if depth == 0 or IsTerminalNode(board, player):
#         return EvalBoard(board, player)
#     if maximizingPlayer:
#         v = minEvalBoard
#         for y in range(n):
#             for x in range(n):
#                 if ValidMove(board, x, y, player):
#                     (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
#                     v = max(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, False))
#                     alpha = max(alpha, v)
#                     if beta <= alpha:
#                         break  # beta cut-off
#         return v
#     else:  # minimizingPlayer
#         v = maxEvalBoard
#         for y in range(n):
#             for x in range(n):
#                 if ValidMove(board, x, y, player):
#                     (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
#                     v = min(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, True))
#                     beta = min(beta, v)
#                     if beta <= alpha:
#                         break  # alpha cut-off
#         return v
