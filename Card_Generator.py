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



