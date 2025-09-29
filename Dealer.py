import random
used_cards = set()
def gen_dealer():
    while True:
        card = (
            random.randint(1, 13),
            random.choice(['Hearts', 'Diamonds', 'Clubs', 'Spades'])
        )
        if card not in used_cards:
            used_cards.add(card)
            return card



for i in range(50):
    gen_dealer()
    print(i+1)

print(used_cards) 