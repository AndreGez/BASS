from enum import Enum
import numpy as np
import pandas as pd


class Color(Enum):
    BASS = 0
    CLUBS = 1
    DIAMOND = 2
    HEART = 3
    SPADES = 4


class Value(Enum):
    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12


class Card:
    col: Color
    val: Value
    isTrump: bool

    def __init__(self, color, value, isTrump = False):
        self.col = color
        self.val = value
        self.isTrump = isTrump

    def Fight(self, opponent) -> bool:
        if self.isTrump and not opponent.isTrump:
            return True
        
        if opponent.isTrump and not self.isTrump:
            return False
        
        if self.col is not opponent.col:
            return False
        
        return self.val > opponent.val


class Game:
    pile: np.array(dtype=Card)
    trump: Color
    players: int
    cardsPerPlayer: int

    def __init__(self, players = 2, cardsPerPlayer = 6, seed = None):
        if seed is not None:
            np.random.seed(seed)

        self.players = players
        self.cardsPerPlayer = cardsPerPlayer

        pile = np.empty()
        trump = np.random.randint(0, Enum.GetValues(type(Color)).Cast<Color>().Max())

        for c in Color:
            for v in Value:
                pile.append(Card(c, v, trump == c))

        np.random.shuffle(pile)


    #def Deal(self) -> np.array(dtype=Card):


    def Next(self) -> Card:
        return self.pile.pop(self.pile.Last())
