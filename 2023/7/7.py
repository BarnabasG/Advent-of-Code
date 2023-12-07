
card_ranks = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
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
    #print(hand)
    score = hand_type(hand)*(13**5)
    for i, card in enumerate(hand[::-1]):
        #print(i,card,card_ranks[card],card_ranks[card]*(13**i))
        score += card_ranks[card]*(13**i)
        # score += card_ranks[card]+(13**i)
    #print(score)
    #print()
    return score



def hand_type(hand):
    counts = [hand.count(card) for card in card_ranks]
    #print(hand, counts)
    if 5 in counts:
        return 7
    elif 4 in counts:
        return 6
    elif 3 in counts and 2 in counts:
        return 5
    elif 3 in counts:
        return 4
    elif counts.count(2) == 2:
        return 3
    elif 2 in counts:
        return 2
    else:
        return 1


# def get_answer(filename='input.txt'):
#     lines = parse_input('2023/7/'+filename)
#     hands = separate_lines(lines)
#     # scores = [(score_hand(k),v,k) for k,v in hands]
#     scores = [(score_hand(k),v) for k,v in hands]
#     print(scores)
#     scores.sort(key=lambda x: x[0], reverse=False)
#     print(scores)
#     scores = [scores[i][1]*(i+1) for i in range(len(scores))]
#     print(scores)
#     return sum(scores)

def get_answer(filename='input.txt'):
    lines = parse_input('2023/7/'+filename)
    hands = separate_lines(lines)
    scores = sorted([(score_hand(k),v) for k,v in hands], key=lambda x: x[0], reverse=False)
    return sum([scores[i][1]*(i+1) for i in range(len(scores))])


answer = get_answer()#'test_input.txt')
print(answer)