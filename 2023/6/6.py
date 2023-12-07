import re
import math
from numpy import prod

def get_answer(filename='input.txt'):
    with open('2023/6/'+filename, 'r') as f:
        times = [int(x) for x in re.findall(r'\d+', f.readline().rstrip('\n'))]
        distances = [int(x) for x in re.findall(r'\d+', f.readline().rstrip('\n'))]

    wins = []
    for time,distance in zip(times,distances):
        disc = (time**2) - (4*distance)
        wins.append(math.ceil(abs(((-time-math.sqrt(disc))/2) - ((-time+math.sqrt(disc))/2))))
    return prod(wins)

answer = get_answer()
print(answer)