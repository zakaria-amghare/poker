import random
from Classes.card import Card
from termcolor import cprint

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

def show_card(cardlist: list[Card]):
    for card in cardlist:
        suit = card[1]  # Assuming card is like ('A', 'Hearts') or ('10', 'Spades')
        if suit == "Hearts":
            cprint(card, "red")
        elif suit == "Diamonds":
            cprint(card, "magenta")
        elif suit == "Clubs":
            cprint(card, "green")
        elif suit == "Spades":
            cprint(card, "blue")
        else:
            print("error: unknown suit", suit)