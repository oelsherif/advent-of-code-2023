from collections import Counter
with open("inputs/07.txt", "r") as File:
    lines = [line.split() for line in File]


def hand_type(hand):
    '''Takes hand and return its type, with 5 of a kind getting rank 6, and high card getting rank 0'''
    freq = sorted(Counter(hand).values(), reverse = True)
    if freq[0] == 5:
        return 6
    elif freq[0] == 4:
        return 5
    elif freq[0] == 3 and freq[1] == 2:
        return 4
    elif freq[0] == 3:
        return 3
    elif freq[0] == 2 and freq[1] == 2:
        return 2
    elif freq[0] == 2:
        return 1
    return 0

def hand_value(hand):
    '''Treats the hand as a base 13 number, and return its value'''
    val = 0
    for i, card in enumerate(hand[::-1]):
        val += card_value[card] * 13 ** i
    return val

def strength(hand):
    """returns the overall strength of the hand, based on type then value"""
    return hand_type(hand) * max_hand_value + hand_value(hand)

max_hand_value = 13 ** 5
card_value = {card: i for i, card in enumerate("23456789TJQKA")}
bids = {line[0]: int(line[1]) for line in lines}
strengths = {hand: strength(hand) for hand in bids.keys()}

# Sort hands by strength, lowest to highest
sorted_hands = sorted(strengths.keys(), key = strengths.get)

ans = 0
for i, hand in enumerate(sorted_hands):
    ans += (i + 1) * bids[hand]

print(ans)