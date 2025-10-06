import random
from Classes.card import Card

used_cards : set[Card] = set()
def gen_card():
    while True:
        card:Card = Card(
            random.randint(2, 14),
            random.choice(['Hearts', 'Diamonds', 'Clubs', 'Spades'])
        )
        if card not in used_cards:
            used_cards.add(card)
            return card

def gen_hand():
    return [gen_card() for _ in range(2)]
def gen_flop():
    return [gen_card() for _ in range(3)]
def gen_turn():
    return [gen_card() for _ in range(1)]
def gen_river():
    return [gen_card() for _ in range(1)]

def reset():
    used_cards.clear()