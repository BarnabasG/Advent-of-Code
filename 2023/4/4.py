import re

def get_score(win, mine):
    c = sum(el in mine for el in win)
    return 0 if c==0 else 2**(c-1)

def get_answer(filename='2023/4/input.txt'):
    score = 0
    with open(filename) as f:
        for line in f:
            w,m = line.split(':')[1].split('|')
            winning_numbers = re.findall(r'\d+', w)
            my_numbers = re.findall(r'\d+', m)
            score += get_score(winning_numbers, my_numbers)
    
    return score


answer = get_answer()
print(answer)