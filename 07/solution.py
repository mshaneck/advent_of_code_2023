
# 5 of a kind through high card
hands = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

def get_hand_rank(hand):
    # return the base rank for the hand
    # from 1 to 7, 1 being 5 of a kind, 7 being high card
    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    # 5 of a kind
    if len(cards) == 1:
        return 1

    # either full house of 4 of a kind
    if len(cards) == 2:
        for card in cards:
            # 4 of a kind
            if cards[card] == 4:
                return 2

            # full house
            if cards[card] == 3:
                return 3

    # either 3 of a kind or 2 pair
    if len(cards) == 3:
        for card in cards:

            # 3 of a kind
            if cards[card] == 3:
                return 4

            if cards[card] == 2:
                return 5

    # one pair
    if len(cards) == 4:
        return 6
    # high card
    if len(cards) == 5:
        return 7

    print("This should not happen. It did for hand: " + hand)
    return -1

def is_higher_card(c1, c2):
    # is c1 higher than c2
    card_ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    c1_index = card_ranks.index(c1)
    c2_index = card_ranks.index(c2)
    return c1_index - c2_index

def is_higher_subrank(hand1, hand2):
    # is hand1 a higher hand than hand2
    if len(hand1) != len(hand2):
        print("This should not happen: " + hand1 + " / " + hand2)
    for i in range(len(hand1)):
        comp = is_higher_card(hand1[i], hand2[i])
        if comp < 0:
            return True
        if comp > 0:
            return False

    print("This should never happen. It did while comparing subrank of " + hand1 + " and " + hand2)
    return True

def insert_hand(hand_tuple, rank):
    # insert the hand into the list, sorted with highest subrank first
    global hands
    index = len(hands[rank])
    for i in range(len(hands[rank])):
        if is_higher_subrank(hand_tuple[0], hands[rank][i][0]):
            index = i
            break
    if index == len(hands[rank]):
        hands[rank] = hands[rank][:index] + [hand_tuple]
    else:
        hands[rank] = hands[rank][:index] + [hand_tuple] + hands[rank][index:]

with open("puzzle_input.txt", "r") as inp:
    for line in inp:
        (hand, bid) = line.split()
        rank = get_hand_rank(hand)
        insert_hand((hand, int(bid)), rank)

    #print(hands)
    overall_rank = []
    total_length = 0
    for i in hands:
        total_length += len(hands[i])
        overall_rank.extend(hands[i])
    #print(overall_rank)
    worth = 0
    for i in range(total_length):
        worth += (total_length-i)*overall_rank[i][1]
    print(worth)
    
