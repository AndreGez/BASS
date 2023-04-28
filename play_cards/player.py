from card import Color
from table import Table
from legal import legal_attacking, legal_defending
import random
from abc import ABC, abstractmethod

class Player(ABC):
    hand: list
    trump: Color
    table: Table
    name: str

    def __init__(self, name):
        self.hand = []
        self.trump = None
        self.table = None
        self.name = name

    def SetTrump(self, trump):
        self.trump = trump

    def SetTable(self, table):
        self.table = table

    def AcceptCards(self, cards):
        self.hand += cards

    def GetHand(self):
        return self.hand
    
    @abstractmethod
    def Attack(self):
        pass

    @abstractmethod
    def Defend(self):
        pass
                
    
    def PickUp(self):
        self.hand += self.table.pick_up_cards()
