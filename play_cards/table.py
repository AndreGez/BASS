from card import Color, Value, Card
import numpy as np

class Table():
    pile: list
    attacking: list
    discarded_cards: list
    trump: Color
    num_cards: int

    def __init__(self):
        self.pile = []        

        for c in Color:
            for v in Value:
                if v.value > 0:
                    self.pile.append(Card(c, v))
        self.num_cards = len(self.pile)
        np.random.shuffle(self.pile)
        self.trump = self.pile[0].col
        self.attacking = []
        self.discarded_cards = []

    def attack(self, cards):
        for card in cards:
            self.attacking.append(tuple([card, None]))

    def defend(self, attacking_card: Card, defending_card: Card):
        for idx, (att_card, def_card) in enumerate(self.attacking):
            if att_card == attacking_card:
                self.attacking[idx] = tuple([att_card, defending_card])
                break

    def cards_to_defend(self):
        return [att_card for att_card, def_card in self.attacking if def_card is None]

    def pick_up_cards(self):
        res = []
        for att_card, def_card in self.attacking:
            res.append(att_card)
            if def_card is not None:
                res.append(def_card)
        self.attacking = []
        return res

    def DrawNextCards(self, number) -> Card:
        res = []
        for idx in range(number):
            if len(self.pile) != 0:
                res.append(self.pile.pop())
        return res
    
    def DiscardCards(self):
        for att in self.attacking:
            self.discarded_cards.append(att[0])
            self.discarded_cards.append(att[1])
            self.attacking.remove(att)