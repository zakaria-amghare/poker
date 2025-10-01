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