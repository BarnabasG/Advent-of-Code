import re
from math import lcm
from functools import reduce

def parse_input(filename):
    with open(filename, 'r') as f:
        directions = f.readline().rstrip('\n').replace('L', '0').replace('R', '1')
        f.readline()
        instructions = {x[0]: (x[1],x[2]) for x in [parse_instructions(line.rstrip('\n')) for line in f.readlines()]}
        return directions, instructions
    
def parse_instructions(instruction):
    return re.findall(r'\w+', instruction)

def get_steps_to_z(m, node, directions):
    steps = 0
    while node[2] != 'Z':
        node = m[node][int(directions[steps%len(directions)])]
        steps += 1
    return steps


def get_answer(filename='input.txt'):
    directions, m = parse_input('2023/8/'+filename)
    return reduce(lcm, [get_steps_to_z(m, node, directions) for node in m.keys() if node[2] == 'A'])

answer = get_answer()#'test_input.txt')
print(answer)