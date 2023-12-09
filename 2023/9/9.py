import re

def parse_input(filename):
    with open(filename, 'r') as f:
        return [[int(x) for x in re.findall(r'-?\d+', line)] for line in f.readlines()]

def get_diflist(l):
    return [l[i+1]-l[i] for i in range(len(l)-1)]

def backtrack(diflists):
    hold = 0
    for list in diflists[::-1]:
        hold = list[-1] + hold
    return hold

def get_answer(filename='input.txt'):
    lines = parse_input('2023/9/'+filename)
    next_vals = []
    for line in lines:
        diflists = [line]
        while True:
            diflists.append(get_diflist(diflists[-1]))
            if diflists[-1].count(diflists[-1][0]) == len(diflists[-1]):
                break
        next_vals.append(backtrack(diflists))
    return sum(next_vals)

answer = get_answer()#'test_input.txt')
print(answer)