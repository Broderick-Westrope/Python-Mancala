from players import Human, RandomAI, MonteCarloAI
from helper import CoinToss
from board import Board


class Mancala:
    def __init__(self, p1, p2):
        self.players = [None] * 2
        self.players[0] = p1
        self.players[1] = p2

    def Begin(self, board):
        self.turn = CoinToss()
        while not self.IsGameOver():
            player = self.players[self.turn]
            print("\n" + player.name + "'s Turn:")
            # self.PrintBoard()
            self.PrintValues()  # TODO - Change this to print the values on the board
            index = player.GetMove()
            self.PlaceMove(index)
            self.turn = (0 if self.turn == 1 else 1)
        self.DeclareWinner()

    def PlaceMove(self, index):
        p = self.turn  # This is the index of the player who we are giving stones to currently
        print(self.players[p].name + " played " + str(index+1))
        stonesToPlay = self.players[p].GetStones(index)
        while stonesToPlay > 0:
            index += 1
            if index > 6:
                index = 0
                p = (0 if p == 1 else 1)
            self.players[p].pockets[index] += 1
            stonesToPlay -= 1

    def IsGameOver(self):
        return self.players[0].AllEmpty() or self.players[1].AllEmpty()

    def DeclareWinner(self):
        print("")
        if self.players[0].AllEmpty():
            print(self.players[0].name + " ran out of stones.")
        elif self.players[1].AllEmpty():
            print(self.players[1].name + " ran out of stones.")
        else:
            print("** ERROR: No one ran out of stones. **")
        p1Score = self.players[0].pockets[6]
        p2Score = self.players[1].pockets[6]
        if p1Score > p2Score:
            print(self.players[0].name + " won the game!")
        elif p1Score < p2Score:
            print(self.players[1].name + " won the game!")
        else:
            print("It was a draw!")
        print("\nFinal Board:")
        self.PrintValues()

    def PrintValues(self):
        playerLine = (str(self.players[0].name) + " \t" +
                      "  M:" + str(self.players[0].pockets[6]) +
                      "  6:" + str(self.players[0].pockets[5]) +
                      "  5:" + str(self.players[0].pockets[4]) +
                      "  4:" + str(self.players[0].pockets[3]) +
                      "  3:" + str(self.players[0].pockets[2]) +
                      "  2:" + str(self.players[0].pockets[1]) +
                      "  1:" + str(self.players[0].pockets[0]))
        print(playerLine)
        playerLine = (str(self.players[1].name) + " \t" +
                      "  1:" + str(self.players[1].pockets[0]) +
                      "  2:" + str(self.players[1].pockets[1]) +
                      "  3:" + str(self.players[1].pockets[2]) +
                      "  4:" + str(self.players[1].pockets[3]) +
                      "  5:" + str(self.players[1].pockets[4]) +
                      "  6:" + str(self.players[1].pockets[5]) +
                      "  M:" + str(self.players[1].pockets[6]))
        print(playerLine)

    def PrintBoard(self):
        # region - Top Row (Top of Board)
        print("+", end='')
        for i in range(99):
            print("-", end='')
        print("+")
        # endregion

        # region - Rows of Pocket (x2)
        for l in range(2):
            # region - Top of the Pockets
            # region - Top of Left Mancala
            if(l == 0):
                print("| +", end='')
                for i in range(13):
                    print("-", end='')
                print("+ ", end='')
            else:
                print("| |", end='')
                for i in range(13):
                    print(" ", end='')
                print("| ", end='')
            # endregion
            # region - Top of Pockets
            for i in range(6):
                print("+", end='')
                for j in range(8):
                    print("-", end='')
                print("+ ", end='')
            # endregion
            # region - Top of Right Mancala
            if(l == 0):
                print("+", end='')
                for i in range(13):
                    print("-", end='')
                print("+ |")
            else:
                print("|", end='')
                for i in range(13):
                    print(" ", end='')
                print("| |")
            # endregion
            # endregion

            # region - Middle of the Pockets
            for k in range(3):
                # region - Left Mancala
                print("| |", end='')
                for i in range(13):
                    print(" ", end='')
                print("| ", end='')
                # endregion

                # region - Pockets
                for i in range(6):
                    print("|", end='')
                    for j in range(8):
                        print(" ", end='')
                    print("| ", end='')
                # endregion

                # region - Right Mancala
                print("|", end='')
                for i in range(13):
                    print(" ", end='')
                print("| |")
                # endregion
            # endregion

            # region - Bottom of the Pockets
            # region - Left Mancala
            if l == 0:
                print("| |", end='')
                for i in range(13):
                    print(" ", end='')
                print("| ", end='')
            else:
                print("| +", end='')
                for i in range(13):
                    print("-", end='')
                print("+ ", end='')
            # endregion
            # region - Top of the Pockets
            for i in range(6):
                print("+", end='')
                for j in range(8):
                    print("-", end='')
                print("+ ", end='')
            # endregion
            # region - Right Mancala
            if l == 0:
                print("|", end='')
                for i in range(13):
                    print(" ", end='')
                print("| |")
            else:
                print("+", end='')
                for i in range(13):
                    print("-", end='')
                print("+ |")
            # endregion
            # endregion
            # endregion

        # region - Bottom Row (Bottom of Board)
        print("+", end='')
        for i in range(99):
            print("-", end='')
        print("+")
        # endregion


if __name__ == '__main__':
    p1 = RandomAI(0, "Brodie")
    p2 = RandomAI(1, "Fred")
    game = Mancala(p1, p2)
    game.Begin()
