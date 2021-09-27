from player import Player
from helper import Controller
from mancala import Mancala


def Menu():
    mode = input("Would you like to play a [G]ame or see a [S]imulation? ")
    if mode == "G" or mode == "g":
        print("Beginning a game...")
        Game()
    elif mode == "S" or mode == "s":
        print("Beginning a simulation...")
        Simulation()


def Game():
    name = input("What's your name? ")
    startingStones = GetStartingStones()
    p1 = Player(startingStones, name, Controller.human)
    p2Controller = GetController(
        "Would you like your opponent to be [H]uman, [R]andom-Choice AI, or [M]onte-Carlo AI? ")
    name = input("What's your opponents name? ")
    p2 = Player(startingStones, name, p2Controller)
    game = Mancala(p1, p2)
    game.Begin()


def Simulation():
    pass


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


def GetController(message, canBeHuman=True):
    while True:
        val = input(message)
        if canBeHuman and (val == "H" or val == "h"):
            return Controller.human
        elif val == "R" or val == "r":
            return Controller.random
        elif val == "M" or val == "m":
            return Controller.monteCarlo
        else:
            print("** Please enter a valid option **")


if __name__ == '__main__':
    Menu()
