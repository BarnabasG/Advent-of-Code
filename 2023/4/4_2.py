import re
from collections import deque

def get_count(win, mine):
    return sum(el in mine for el in win)

def get_answer(filename='2023/4/input.txt'):
    next_multipliers = deque([1]*10)
    multiplier = 1
    total = 0
    with open(filename) as f:
        for line in f:
            w,m = line.split(':')[1].split('|')
            winning_numbers = re.findall(r'\d+', w)
            my_numbers = re.findall(r'\d+', m)
            total += multiplier

            c = get_count(winning_numbers, my_numbers)
            for i in range(c):
                next_multipliers[i] += multiplier
            multiplier = next_multipliers.popleft()
            next_multipliers.append(1)
    
    return total


answer = get_answer()
print(answer)