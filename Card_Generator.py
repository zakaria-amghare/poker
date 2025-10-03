import random
from card import Card

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




def gen_hand(num_cards=2):
    return [gen_card() for _ in range(num_cards)]
def flop():
    return [gen_card() for _ in range(3)]
def turn():
    return [gen_card() for _ in range(1)]
def river():
    return [gen_card() for _ in range(1)]