from players import Human, RandomAI, MonteCarloAI
from mancala import Mancala
from board import Board


def Menu():
    mode = input("Would you like to play a [G]ame or see a [S]imulation? ")
    if mode == "G" or mode == "g":
        print("Beginning a game...")
        Game()
    elif mode == "S" or mode == "s":
        print("Beginning a simulation...")
        Simulation()


def Game():
    startingStones = GetStartingStones()

    name = input("What's your name? ")
    p1 = Human(0, name)

    name = input("What's your opponents name? ")
    p2 = GetPlayer(
        1, name, "Would you like your opponent to be [H]uman, [R]andom-Choice AI, or [M]onte-Carlo AI? ")
    game = Mancala(p1, p2)
    game.Begin(Board(startingStones))


def Simulation():
    startingStones = GetStartingStones()

    name = input("What's the name of Player 1? ")
    p1 = RandomAI(0, name)
    name = input("What's the name of Player 2? ")
    p2 = RandomAI(1, name)
    game = Mancala(p1, p2)
    game.Begin(Board(startingStones))


def GetStartingStones():
    while True:
        startingStones = input(
            "How many stones should each pocket start with? (Default is 4) ")
        try:
            startingStones = int(startingStones)
            if(startingStones <= 0):
                raise ValueError("Not a positive number.")
            break
        except ValueError:
            print("** Please enter a positive integer **")
    return startingStones


def GetPlayer(id, name, message, canBeHuman=True):
    while True:
        val = input(message)
        if canBeHuman and (val == "H" or val == "h"):
            return Human(id, name)
        elif val == "R" or val == "r":
            return RandomAI(id, name)
        elif val == "M" or val == "m":
            return MonteCarloAI(id, name)
        else:
            print("** Please enter a valid option **")


if __name__ == '__main__':
    Menu()
