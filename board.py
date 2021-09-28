from copy import copy


class Board:
    def __init__(self, startingStones=4):
        self.pockets = [[startingStones for i in range(6)] for j in range(2)]
        self.mancala = [0] * 2

    def GetStones(self, pid, index):
        stones = copy(self.pockets[pid][index])
        self.pockets[pid][index] = 0
        return stones

    def AllEmpty(self, pid):
        for i in range(6):
            if self.pockets[pid][i] > 0:
                return False
        return True

    def PlaceMove(self, pid, index):
        # This is the index of the player who we are giving stones to currently
        p = copy(pid)
        stonesToPlay = self.GetStones(pid, index)
        while stonesToPlay > 0:
            index += 1
            if index > 6:
                index = 0
                p = (0 if p == 1 else 1)
            if index == 6:
                self.mancala[p] += 1
            else:
                self.pockets[p][index] += 1
            stonesToPlay -= 1

    def IsGameOver(self):
        return self.AllEmpty(0) or self.AllEmpty(1)

    def DeclareWinner(self, p1Name, p2Name):
        print("")
        if self.AllEmpty(0):
            print(p1Name + " ran out of stones.")
        elif self.AllEmpty(1):
            print(p2Name + " ran out of stones.")
        else:
            print("** ERROR: No one ran out of stones. **")

        p1Score = self.mancala[0]
        p2Score = self.mancala[1]
        if p1Score > p2Score:
            print(p1Name + " won the game!")
        elif p1Score < p2Score:
            print(p2Name + " won the game!")
        else:
            print("It was a draw!")
        print("\nFinal Board:")
        self.PrintValues(p1Name, p2Name)

    def PrintValues(self, p1Name, p2Name):
        playerLine = (str(p1Name) + " \t" +
                      "  M:" + str(self.mancala[0]) +
                      "  6:" + str(self.pockets[0][5]) +
                      "  5:" + str(self.pockets[0][4]) +
                      "  4:" + str(self.pockets[0][3]) +
                      "  3:" + str(self.pockets[0][2]) +
                      "  2:" + str(self.pockets[0][1]) +
                      "  1:" + str(self.pockets[0][0]))
        print(playerLine)
        playerLine = (str(p2Name) + " \t" +
                      "  1:" + str(self.pockets[1][0]) +
                      "  2:" + str(self.pockets[1][1]) +
                      "  3:" + str(self.pockets[1][2]) +
                      "  4:" + str(self.pockets[1][3]) +
                      "  5:" + str(self.pockets[1][4]) +
                      "  6:" + str(self.pockets[1][5]) +
                      "  M:" + str(self.mancala[1]))
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
