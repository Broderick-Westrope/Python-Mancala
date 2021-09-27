from enum import Enum
import random


class Controller(Enum):
    human = 1
    random = 2
    monteCarlo = 3


def CoinToss():
    print("Flipping a coin to decide who's first...")
    return random.randint(0, 1)
