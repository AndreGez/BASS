def legal_attacking(hand_cards, attacking_cards):
    if len(attacking_cards) == 0:
        return hand_cards
    legal_cards = []
    for h_card in hand_cards:
        for a_card, a_card2 in attacking_cards:
            if h_card.val == a_card.val:
                legal_cards.append(h_card)
                break
            if a_card2 is not None:
                if h_card.val == a_card2.val:
                    legal_cards.append(h_card)
                    break
    return legal_cards

def legal_defending(hand_cards, attacking_cards, trump):
    options = dict()
    for a_card, a_card2 in attacking_cards:
        if a_card2 is None:
            options[a_card] = []
            for h_card in hand_cards:
                if can_defend(h_card, a_card, trump):
                    options[a_card].append(h_card)
    return options

def can_shift(hand_cards, attacking_cards):
    for h_card in hand_cards:
        for a_card in attacking_cards:
            if h_card.val == a_card.val:
                return True
            
def can_defend(hand_card, attacking_card, trump):
    if hand_card.col == trump and attacking_card.col != trump:
        return True
    if hand_card.col == attacking_card.col and hand_card.val.value > attacking_card.val.value:
        return True
    return False
