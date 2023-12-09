import os
import re
from collections import Counter

script_dir = os.path.dirname(__file__)

relative_path = os.path.join(script_dir, 'inputs', '7.txt')

def classify_cards(card):
    # hand_priority = {'five of a kind':6, 'four of a kind':5, 'full house':4, 'three of a kind':3, 'two pair':2, 'one pair':1, 'high card':0}
    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
    # Return hand type and highest card
    cards = [i for i in card]
    counter = Counter(cards)
    card_counts = counter.most_common()
    card_counts = adjust_jacks(cards, card_counts)
    card_value = {'A':13, 'K':12, 'Q':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J':1}
    cards = [card_value[i] for i in cards]
    if card_counts[0][1] == 5:
        return 6, cards
    elif card_counts[0][1] == 4:
        return 5, cards
    elif card_counts[0][1] == 3 and card_counts[1][1] == 2:
        return 4, cards
    elif card_counts[0][1] == 3:
        return 3, cards
    elif card_counts[0][1] == 2 and card_counts[1][1] == 2:
        return 2, cards
    elif card_counts[0][1] == 2:
        return 1, cards
    else:
        return 0, cards

def adjust_jacks(cards, card_counts):
    # Jacks serve to maximize the value of a hand
    if sum([True for card, count in card_counts if card == 'J']) != 0:
        # Jack is present
        cards = [card_counts[0][0] if card == 'J' else card for card in cards]
        counter = Counter(cards)
        card_counts = counter.most_common()
    return card_counts

def rank_cards(cards):
    cards = [classify_cards(card) for card in cards]
    rank = rank_vector(cards)
    return rank

def rank_vector(vector):
    # Sort the vector and get the indices
    sorted_vector = sorted(enumerate(vector), key=lambda x: x[1])
    ranked_vector = [(index, rank+1) for rank, (index, value) in enumerate(sorted_vector)]
    ranked_vector.sort()
    rank = [rank for index, rank in ranked_vector]
    return rank

cards = []
bids = []
with open(relative_path, 'r') as file:
    for line in file:
        card = re.findall(r'^([A-Z0-9]{5}) ', line)[0]
        bid = int(re.findall(r' (\d+)', line)[0])
        cards.append(card)
        bids.append(bid)

ranks = rank_cards(cards)

print(sum([rank * bid for rank, bid in zip(ranks, bids)]))
