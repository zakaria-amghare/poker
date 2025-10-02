import Calculate_Winner

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
    if Calculate_Winner.royal_flush(hand):
        print(f"Hand: {hand} is a Royal Flush")
        return  hand_rankings["Royal Flush"]
    elif Calculate_Winner.straight_flush(hand):
        print(f"Hand: {hand} is a Straight Flush")
        return hand_rankings["Straight Flush"]
    elif Calculate_Winner.four_of_a_kind(hand):
        print(f"Hand: {hand} is a Four of a Kind")
        return hand_rankings["Four of a Kind"]
    elif Calculate_Winner.full_house(hand):
        print(f"Hand: {hand} is a Full House")
        return hand_rankings["Full House"]
    elif Calculate_Winner.flush(hand):
        print(f"Hand: {hand} is a Flush")
        return hand_rankings["Flush"]
    elif Calculate_Winner.straight(hand):
        print(f"Hand: {hand} is a Straight")
        return hand_rankings["Straight"]
    elif Calculate_Winner.three_of_a_kind(hand):
        print(f"Hand: {hand} is a Three of a Kind")
        return hand_rankings["Three of a Kind"]
    elif Calculate_Winner.two_pair(hand):
        print(f"Hand: {hand} is a Two Pair")
        return hand_rankings["Two Pair"]
    elif Calculate_Winner.one_pair(hand):
        print(f"Hand: {hand} is a One Pair")
        return hand_rankings["One Pair"]
    else:
        return hand_rankings["High Card"]