from PlayerControllers.players import Player
from copy import deepcopy
from heapq import heappush, heappop, heapify
from random import choice


class MonteCarloAI(Player):
    def __init__(self, id, name="Monte-Carlo AI"):
        super().__init__(id, name=name)
        self.oppId = 1 if self.id == 0 else 0

    def GetMove(self, board):
        moves = []
        print("Values of moves:")

        for m in range(6):
            print("Pocket " + str(m+1) + ": ", end='')
            if board.pockets[self.id][m] == 0:
                print("*Empty*")
                continue

            tempBoard = deepcopy(board)
            tempBoard.PlaceMove(self.id, m)

            if tempBoard.IsGameOver():
                result = self.Evaluation(tempBoard)
                if result == 1:
                    print("*Winning Move*")
                    return m
                elif result == -1:
                    print("*Losing Move*")
                    continue
                else:
                    print("*Draw Move*")
                    heappush(moves, (0, m))
                    continue

            value = self.Simulation(tempBoard)
            heappush(moves, (value, m))
            print(value)

        if not len(moves) == 0:
            print("Best Value: " +
                  str(moves[0][0]) + "(Pocket " + str(moves[0][1]) + ")")
            return moves[0][1]

        print("** ERROR: No moves were found by Monte-Carlo AI. **")
        return -1

    def Simulation(self, board):
        winning = 0.0
        times = 100  # 2500
        for i in range(times):
            # print("")
            # board.PrintValues("1", "2")
            # print("")
            tempBoard = deepcopy(board)
            winning += self.Expansion(self.oppId, tempBoard, 0)
        return (winning / times)

    def Expansion(self, player, board, depth):
        randMove = self.GetRandomMove(board)
        board.PlaceMove(player, randMove)

        if board.IsGameOver():
            result = self.Evaluation(board)
            if result == 1:
                return 1.0 - depth
            elif result == -1:
                return -1.0 - depth
            else:
                return 0 - depth

        player = (self.id if player == self.oppId else self.oppId)
        return self.Expansion(player, board, depth + 0.05)

    def GetRandomMove(self, board):
        candidates = list(range(6))
        while True:
            m = choice(candidates)
            if board.pockets[self.id][m] <= 0:
                candidates.remove(m)
            else:
                return m

    def Evaluation(self, board):
        if board.mancala[self.id] > board.mancala[self.oppId]:
            return 1
        elif board.mancala[self.id] < board.mancala[self.oppId]:
            return 2
        else:
            return 0
