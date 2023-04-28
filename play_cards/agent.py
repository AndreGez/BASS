from player import Player

import numpy as np

class Agent(Player):
    def __init__(self, name):
        super().__init__(name)

    def Attack(self):
        pass

    def Defend(self):
        pass

    def CreateFeatures(self, attacking):
        # one field for each card in the game, one for trump color, one for attacking or defending
        features = np.zeros(self.table.num_cards + 2)
        for card in self.hand:
            features[card.GetIndex()] = 1
        for card in self.table.discarded_cards:
            features[card.GetIndex()] = 2
        if len(self.table.pile > 0):
            features[self.table.pile[0].GetIndex()] = 3
        features[-2] = self.trump.value
        features[-1] = attacking