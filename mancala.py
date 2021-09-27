from player import Player
from helper import CoinToss


class Mancala:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def Begin(self):
        self.turn = CoinToss()
        while not self.IsGameOver():
            player = (self.p1.name if self.turn == 0 else self.p2.name)
            print(player + "'s Turn:")
            self.PrintBoard()
            input("")
            self.turn = (0 if self.turn == 1 else 1)

    def IsGameOver(self):
        return self.p1.AllEmpty() or self.p2.AllEmpty()

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
    p1 = Player()
    p2 = Player()
    game = Mancala(p1, p2)
    game.PrintBoard()
