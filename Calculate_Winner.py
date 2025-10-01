def royal_flush(hand):
    suits =  {'Hearts': [], 'Diamonds': [], 'Clubs': [], 'Spades': []}
    for card in hand:
        suits[card[1]].append(card[0])
    for suit, ranks in suits.items():
        if all(rank in ranks for rank in [10, 11, 12, 13, 14]):
            return True
    return False

def straight_flush(hand):
    # Group cards by suit
    suits = {}
    for card in hand:
        suit = card[1]
        if suit not in suits:
            suits[suit] = []
        suits[suit].append(card[0])
        if card[0] == 14:  
            suits[suit].append(1)
    
    # Check each suit that has at least 5 cards
    for suit, ranks in suits.items():
        if len(ranks) >= 5:
            # Sort ranks for this suit
            ranks.sort()
            
            # Check for 5 consecutive cards
            for i in range(len(ranks) - 4):
                is_straight = True
                for j in range(4):
                    if ranks[i + j] + 1 != ranks[i + j + 1]:
                        is_straight = False
                        break
                
                if is_straight:
                    return True

    return False

def four_of_a_kind(hand):
    ranks = [card[0] for card in hand]
    for rank in set(ranks):
        if ranks.count(rank) == 4:
            return True
    return False

def full_house(hand):
    ranks = [card[0] for card in hand]
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    counts = sorted(rank_counts.values(), reverse=True)
    return counts[0] >= 3 and counts[1] >= 2

def flush(hand):
    suits = {}
    for card in hand:
        suit = card[1]
        if suit not in suits:
            suits[suit] = 0
        suits[suit] += 1
    if any(count >= 5 for count in suits.values()):
        return True
    return False

def straight(hand):
    ranks = [card[0] for card in hand]
    ranks = list(set(ranks))  # Remove duplicates
    ranks.sort()
    
    # Check for Ace-low straight (A, 2, 3, 4, 5)
    if set([14, 2, 3, 4, 5]).issubset(ranks):
        return True
    
    for i in range(len(ranks) - 4):
        if ranks[i+4] - ranks[i] == 4:
            return True
    return False

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
    if pairs >= 2:
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