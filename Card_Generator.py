import random
used_cards = set()
def gen_dealer():
    while True:
        card = (
            random.randint(2, 14),
            random.choice(['Hearts', 'Diamonds', 'Clubs', 'Spades'])
        )
        if card not in used_cards:
            used_cards.add(card)
            return card


def gen_player():
    hand = [gen_dealer() for _ in range(5)]
    print(f"Player's hand: {hand}")
    return hand

