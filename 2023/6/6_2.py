import re
import math

def get_answer(filename='input.txt'):
    with open('2023/6/'+filename, 'r') as f:
        time = int(''.join(re.findall(r'\d+', f.readline().rstrip('\n'))))
        distance = int(''.join(re.findall(r'\d+', f.readline().rstrip('\n'))))
    
    disc = (time**2) - (4*distance)
    return math.floor(abs(((-time-math.sqrt(disc))/2) - ((-time+math.sqrt(disc))/2)))

answer = get_answer()
print(answer)

