
card_ranks = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

def parse_input(filename):
    with open(filename, 'r') as f:
        return [line.rstrip('\n') for line in f.readlines()]
    
def separate_lines(lines):
    hands = []
    for line in lines:
        hand,bid = line.split(' ')
        hands.append((hand,int(bid)))
    return hands

def score_hand(hand):
    score = hand_type(hand)*(13**5)
    for i, card in enumerate(hand[::-1]):
        score += card_ranks[card]*(13**i)
    return score

def hand_type(hand):
    counts = [hand.count(card) for card in card_ranks if card != 'J']
    jokers = hand.count('J')
    #print(hand, counts)
    if 5-jokers in counts:
        return 7
    elif 4-jokers in counts:
        return 6
    elif (3 in counts and 2 in counts) or (jokers == 1 and 3 in counts and 1 in counts) or (jokers == 1 and counts.count(2) == 2) or (jokers == 2 and 3 in counts)  or (jokers == 2 and 2 in counts and 1 in counts) or (jokers == 3 and 2 in counts) or (jokers == 3 and counts.count(1) >= 2):
        return 5
    elif 3-jokers in counts:
        return 4
    elif counts.count(2) + jokers == 2 or jokers == 2:
        return 3
    elif 2-jokers in counts:
        return 2
    else:
        return 1

def get_answer(filename='input.txt'):
    lines = parse_input('2023/7/'+filename)
    hands = separate_lines(lines)
    scores = sorted([(score_hand(k),v) for k,v in hands], key=lambda x: x[0], reverse=False)
    return sum([scores[i][1]*(i+1) for i in range(len(scores))])


def run():
    a = get_answer()#'test_input.txt')
    print(a)

def time():
    import timeit
    s = timeit.default_timer()
    for _ in range(100):
        get_answer()
    e = timeit.default_timer() - s
    print(e)
    print(e/100)

run()
#time()