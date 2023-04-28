from enum import Enum

class Color(Enum):
    BASS = 0
    CLUBS = 1
    DIAMOND = 2
    HEART = 3
    SPADES = 4


class Value(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    J = 11
    Q = 12
    K = 13
    A = 14

class Card:
    col: Color
    val: Value

    def __init__(self, color, value):
        self.col = color
        self.val = value

    def __str__(self) -> str:
        return f"{self.col.name}_{self.val.name if self.val.value > 10 else str(self.val.value)}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def GetIndex(self):
        return self.col.value * 13 + self.val.value - 2

