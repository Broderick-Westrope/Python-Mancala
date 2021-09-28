from enum import Enum
import random


def CoinToss():
    print("Flipping a coin to decide who's first...")
    return random.randint(0, 1)
