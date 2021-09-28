from helper import Controller
from copy import copy
from random import choice


class Player:
    def __init__(self, id, name="Player",  startingStones=4):
        self.id = id
        self.name = name
        # 7th Pocket is actually the Mancala
        self.pockets = [startingStones] * 7
        self.pockets[6] = 0

    def AllEmpty(self):
        # print(self.name + ":")
        for i in range(6):
            # print(str(i) + " has " + str(self.pockets[i]))
            if self.pockets[i] > 0:
                return False
        return True

    def GetStones(self, index):
        stones = copy(self.pockets[index])
        self.pockets[index] = 0
        return stones


class Human(Player):
    def __init__(self, id, name="Human", startingStones=4):
        super().__init__(id, name=name, startingStones=startingStones)

    def GetMove(self):
        while True:
            val = input("What pocket would you like to play? (1-6) ")
            try:
                val = int(val)
                if val > 6 or val < 1:
                    raise ValueError(
                        "Out of bounds. Must be in the range 1-6.")
                if self.pockets[val-1] <= 0:
                    raise ValueError("Chose an empty pocket.")
                break
            except ValueError:
                print(
                    "** Please enter an integer between 1 and 6 (inclusive). The pocket must have stones in it. **")  # TODO - Does the pocket NEED stones??
        return (val - 1)


class RandomAI(Player):
    def __init__(self, id, name="Random AI", startingStones=4):
        super().__init__(id, name=name, startingStones=startingStones)

    def GetMove(self):
        candidates = list(range(6))
        while True:
            val = choice(candidates)
            if self.pockets[val] > 0:
                break
        return val


class MonteCarloAI(Player):
    def __init__(self, id, name="Monte-Carlo AI", startingStones=4):
        super().__init__(id, name=name, startingStones=startingStones)

    def BestMove()
