from helper import Controller


class Player:
    def __init__(self,  startingStones=4, name="AI", type=Controller.monteCarlo):
        self.name = name
        self.pockets = [startingStones] * 6
        self.type = type
        self.emptyPockets = 0

    def AllEmpty(self):
        return self.emptyPockets >= len(self.pockets)
