from random import choice


class Player:
    def __init__(self, id, name="Player",  startingStones=4):
        self.id = id
        self.name = name


class Human(Player):
    def __init__(self, id, name="Human", startingStones=4):
        super().__init__(id, name=name, startingStones=startingStones)

    def GetMove(self, board):
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

    def GetMove(self, board):
        candidates = list(range(6))
        while True:
            val = choice(candidates)
            if board.pockets[self.id][val] > 0:
                break
        return val


class MonteCarloAI(Player):
    def __init__(self, id, name="Monte-Carlo AI", startingStones=4):
        super().__init__(id, name=name, startingStones=startingStones)

    def BestMove():
        pass
