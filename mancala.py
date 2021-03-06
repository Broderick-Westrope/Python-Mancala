from PlayerControllers.MonteCarloAI import MonteCarloAI
from PlayerControllers.players import Human, RandomAI
from helper import CoinToss
from board import Board


class Mancala:
    def __init__(self, p1, p2):
        self.players = [None] * 2
        self.players[0] = p1
        self.players[1] = p2

    def Begin(self, board):
        self.turn = CoinToss()
        turnCount = 1
        while not board.IsGameOver():
            player = self.players[self.turn]
            print("\n" + player.name + "'s Turn: \t (Turn " + str(turnCount) + ")")
            # board.PrintBoard()
            # TODO - Change this to print the values on the board
            board.PrintValues(self.players[0].name, self.players[1].name)
            index = player.GetMove(board)
            print(player.name + " played " + str(index+1))
            board.PlaceMove(self.turn, index)
            self.turn = (0 if self.turn == 1 else 1)
            turnCount += 1
        board.DeclareWinner(
            self.players[0].name, self.players[1].name, turnCount)


if __name__ == '__main__':
    p1 = MonteCarloAI(0, "Brodie")
    p2 = MonteCarloAI(1, "Fred")
    game = Mancala(p1, p2)
    game.Begin(Board())
