import re
from functools import cache

def parse_input(filename):
    def separate_lines(l):
        a,b = l.split(' ')
        return (a, tuple(int(x) for x in re.findall(r'\d+',b)))
    with open(filename, 'r') as f:
        return [separate_lines(line.rstrip('\n')) for line in f.readlines()]

@cache
def recurse(line, blocks, result=0):
    if not blocks:
        return '#' not in line
    current, blocks = blocks[0], blocks[1:]
    for i in range(len(line) - sum(blocks) - len(blocks) - current + 1):
        if '#' in line[:i]:
            break
        elif (nxt := current+i) <= len(line) and ('.' not in line[i:nxt]) and (line[nxt:nxt+1] != '#'):
            result += recurse(line[nxt+1:], blocks)
    return result

def get_answer(filename='input.txt'):
    return sum(recurse(line,blocks) for line,blocks in parse_input('2023/12/'+filename))

answer = get_answer()#'test_input.txt')
print(answer)