def royal_flush(hand):
    if hand[0][0] == 14 and hand[1][0] == 13 and hand[2][0] == 12 and hand[3][0] == 11 and hand[4][0] == 10:
        if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
            return True
    return False

def straight_flush(hand):
    hand = sorted(hand, key=lambda x: x[0])
    for i in range(4):
        if hand[i][0] + 1 != hand[i + 1][0] or hand[i][1] != hand[i + 1][1]:
            return False
    return True

def four_of_a_kind(hand):
    ranks = [card[0] for card in hand]
    for rank in set(ranks):
        if ranks.count(rank) == 4:
            return True
    return False

def full_house(hand):
    ranks = [card[0] for card in hand]
    unique_ranks = set(ranks)
    if len(unique_ranks) == 2:
        first_rank = ranks.count(ranks[0])
        if first_rank == 2 or first_rank == 3:
            return True
    return False

def flush(hand):
    suits = [card[1] for card in hand]
    if len(set(suits)) == 1:
        return True
    return False

def straight(hand):
    hand = sorted(hand, key=lambda x: x[0])
    for i in range(4):
        if hand[i][0] + 1 != hand[i + 1][0]:
            return False
    return True

def three_of_a_kind(hand):
    ranks = [card[0] for card in hand]
    for rank in set(ranks):
        if ranks.count(rank) == 3:
            return True
    return False

def two_pair(hand):
    ranks = [card[0] for card in hand]
    pairs = 0
    for rank in set(ranks):
        if ranks.count(rank) == 2:
            pairs += 1
    if pairs == 2:
        return True
    return False

def one_pair(hand):
    ranks = [card[0] for card in hand]
    for rank in set(ranks):
        if ranks.count(rank) == 2:
            return True
    return False

def high_card(hand):
    return max(card[0] for card in hand)




def calculate_winner(player_hands):
    hand_rankings = {
        "Royal Flush": 10,
        "Straight Flush": 9,
        "Four of a Kind": 8,
        "Full House": 7,
        "Flush": 6,
        "Straight": 5,
        "Three of a Kind": 4,
        "Two Pair": 3,
        "One Pair": 2,
        "High Card": 1
    }

    def evaluate_hand(hand):
        if royal_flush(hand):
            return ("Royal Flush", hand_rankings["Royal Flush"])
        elif straight_flush(hand):
            return ("Straight Flush", hand_rankings["Straight Flush"])
        elif four_of_a_kind(hand):
            return ("Four of a Kind", hand_rankings["Four of a Kind"])
        elif full_house(hand):
            return ("Full House", hand_rankings["Full House"])
        elif flush(hand):
            return ("Flush", hand_rankings["Flush"])
        elif straight(hand):
            return ("Straight", hand_rankings["Straight"])
        elif three_of_a_kind(hand):
            return ("Three of a Kind", hand_rankings["Three of a Kind"])
        elif two_pair(hand):
            return ("Two Pair", hand_rankings["Two Pair"])
        elif one_pair(hand):
            return ("One Pair", hand_rankings["One Pair"])
        else:
            return ("High Card", hand_rankings["High Card"])

    best_hand = None
    best_rank = 0
    winner = None

    for player, hand in player_hands.items():
        hand_type, rank = evaluate_hand(hand)
        print(f"{player} has a {hand_type}")
        if rank > best_rank:
            best_rank = rank
            best_hand = hand_type
            winner = player

    print(f"The winner is {winner} with a {best_hand}!")
    return winner, best_hand