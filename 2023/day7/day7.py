#!/usr/bin/env python3

from copy import deepcopy

card_values = {
    '2':1,
    '3':2,
    '4':3,
    '5':4,
    '6':5,
    '7':6,
    '8':7,
    '9':8,
    'T':9,
    'J':10,
    'Q':11,
    'K':12,
    'A':13,
}


p2_card_values = {
    'J':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'Q':11,
    'K':12,
    'A':13,
}

rankings = []
five_ok = []
four_ok = []
fh = []
tok = []
tp = []
op = []
hc = []

def five_of_a_kind(hand) -> bool:
    return len(set(hand)) == 1

def four_of_a_kind(hand) -> bool:
    for char in set(hand):
        if hand.count(char) == 4:
            return True
    return False

def full_house(hand) -> bool:
    vals = set(hand)
    if len(vals) == 2:
        # check if count of either value is 2 or 3
        return hand.count(hand[0]) in [2, 3]
    return False

def three_of_a_kind(hand) -> bool:
    for value in set(hand):
        if hand.count(value) == 3:
            return True
    return False

def two_pair(hand) -> bool:
    values = set(hand)
    pairs_count = 0

    for val in values:
        if hand.count(val) == 2:
            pairs_count += 1
    
    return pairs_count == 2

def one_pair(hand) -> bool:
    val = set(hand)
    pairs_count = 0

    for v in val:
        if hand.count(v) == 2:
            pairs_count += 1
    
    return pairs_count == 1

def high_card(hand) -> bool:
    values = set(hand)
    return len(values) == len(hand)

def gen_hand_conversion(hand):
    num_list = []
    for num in hand[0]:
        num_list.append(card_values[num])

    return num_list

def p2_gen_hand_conversion(hand):
    num_list = []
    for num in hand[0]:
        num_list.append(p2_card_values[num])

    return num_list

def p1(hands):
    total = 0 
    for hand in hands:
        num_list = gen_hand_conversion(hand)
        hand.append(num_list)
        if five_of_a_kind(hand[0]):
            five_ok.append(hand)

        elif four_of_a_kind(hand[0]):
            four_ok.append(hand)

        elif full_house(hand[0]):
            fh.append(hand)

        elif three_of_a_kind(hand[0]):
            tok.append(hand)

        elif two_pair(hand[0]):
            tp.append(hand)
        
        elif one_pair(hand[0]):
            op.append(hand)
        
        else:
            hc.append(hand)

    # sort lists based off lowest starting cards
    sorted_five_ok = sorted(five_ok, key=lambda x: x[2]) 
    sorted_four_ok = sorted(four_ok, key=lambda x: x[2]) 
    sorted_fh = sorted(fh, key=lambda x: x[2]) 
    sorted_tok = sorted(tok, key=lambda x: x[2]) 
    sorted_tp = sorted(tp, key=lambda x: x[2]) 
    sorted_op = sorted(op, key=lambda x: x[2]) 
    sorted_hc = sorted(hc, key=lambda x: x[2]) 

    rankings.extend(sorted_hc)
    rankings.extend(sorted_op)
    rankings.extend(sorted_tp)
    rankings.extend(sorted_tok)
    rankings.extend(sorted_fh)
    rankings.extend(sorted_four_ok)
    rankings.extend(sorted_five_ok)

    for idx, rank in enumerate(rankings):
        total += int(rank[1]) * (idx + 1)

    return total

def joker_count(hand):
    return hand[0].count('J')

def p2(hands):
    # clear lists
    rankings = []
    five_ok = []
    four_ok = []
    fh = []
    tok = []
    tp = []
    op = []
    hc = []

    total = 0 
    for hand in hands:
        num_list = p2_gen_hand_conversion(hand)
        hand.append(num_list)
        jokers = joker_count(hand)

        if five_of_a_kind(hand[0]):
            five_ok.append(hand)

        elif four_of_a_kind(hand[0]):
            if jokers:
                five_ok.append(hand)
            else:
                four_ok.append(hand)

        elif full_house(hand[0]):
            if jokers:
                five_ok.append(hand)
            else:
                fh.append(hand)

        elif three_of_a_kind(hand[0]):
            if jokers == 1:
                four_ok.append(hand)
            elif jokers == 2:
                fh.append(hand)
            elif jokers == 3:
                four_ok.append(hand)
            else:
                tok.append(hand)

        elif two_pair(hand[0]):
            if jokers == 1:
                fh.append(hand)
            elif jokers == 2:
                four_ok.append(hand)
            else:
                tp.append(hand)
        
        elif one_pair(hand[0]):
            if jokers == 1:
                tok.append(hand)
            elif jokers == 2:
                tok.append(hand)
            else:
                op.append(hand)
        
        else:
            if jokers:
                op.append(hand)
            else:
                hc.append(hand)
    
    # sort lists based off lowest starting cards
    sorted_five_ok = sorted(five_ok, key=lambda x: x[2]) 
    sorted_four_ok = sorted(four_ok, key=lambda x: x[2]) 
    sorted_fh = sorted(fh, key=lambda x: x[2]) 
    sorted_tok = sorted(tok, key=lambda x: x[2]) 
    sorted_tp = sorted(tp, key=lambda x: x[2]) 
    sorted_op = sorted(op, key=lambda x: x[2]) 
    sorted_hc = sorted(hc, key=lambda x: x[2]) 

    rankings.extend(sorted_hc)
    rankings.extend(sorted_op)
    rankings.extend(sorted_tp)
    rankings.extend(sorted_tok)
    rankings.extend(sorted_fh)
    rankings.extend(sorted_four_ok)
    rankings.extend(sorted_five_ok)

    for idx, rank in enumerate(rankings):
        total += int(rank[1]) * (idx + 1)

    return total


def main():
    with open("input.txt", "r") as file:
        hands = [line.split() for line in file]
    
    p1_answer = p1(deepcopy(hands))
    print(f"{p1_answer = }")    
    
    p2_answer = p2(deepcopy(hands))
    print(f"{p2_answer = }")

if __name__=="__main__":
    main()