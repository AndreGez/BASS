from card import Color
from table import Table
from legal import legal_attacking, legal_defending
from player import Player
import random
import numpy as np

class PlayerRandom(Player):
    hand: list
    trump: Color
    table: Table
    name: str

    def __init__(self, name):
        super().__init__(name)
    
    def Attack(self):
        self.CreateFeatures(0)
        played_cards = []
        if len(self.table.attacking) == 0:
            card = random.choice(self.hand)
            self.hand.remove(card)
            played_cards.append(card)
            print(self.name, " attacks ", card)
        else:
            possible_moves = legal_attacking(self.hand, self.table.attacking)
            if len(possible_moves) != 0:
                card = random.choice(possible_moves)
                played_cards.append(card)
                self.hand.remove(card)
                print(self.name, " attacks ", card)
        self.table.attack(played_cards)

    def Defend(self):
        self.CreateFeatures(1)
        attacking_cards = self.table.attacking
        def_options = legal_defending(self.hand, attacking_cards, self.trump)
        pick_up = False
        defended_cards = []
        used_cards = []
        for card, options in def_options.items():
            if len(options) == 0:
                pick_up = True
                break
            else:
                choice = random.choice(options)
                if choice not in used_cards:
                    used_cards.append(choice)
                    defended_cards.append((card, choice))
        if pick_up:
            self.PickUp()
        else:
            for card, option in defended_cards:
                print(self.name, " defends ", card, " with ", option)
                self.table.defend(card, option)
                self.hand.remove(option)

    def CreateFeatures(self, attacking):
        # one field for each card in the game, one for trump color, one for attacking or defending
        features = np.zeros(self.table.num_cards + 2, dtype=np.int8)
        for card in self.hand:
            features[card.GetIndex()] = 1
        for card in self.table.discarded_cards:
            features[card.GetIndex()] = 2
        for card_att, card_def in self.table.attacking:
            features[card_att.GetIndex()] = 4
            if card_def is not None:
                features[card_def.GetIndex()] = 5
        if len(self.table.pile) > 0:
            features[self.table.pile[0].GetIndex()] = 3
        features[-2] = self.trump.value
        features[-1] = attacking
        return features