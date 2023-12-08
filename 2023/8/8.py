import re

def parse_input(filename):
    with open(filename, 'r') as f:
        directions = f.readline().rstrip('\n').replace('L', '0').replace('R', '1')
        f.readline()
        instructions = {x[0]: (x[1],x[2]) for x in [parse_instructions(line.rstrip('\n')) for line in f.readlines()]}
        return directions, instructions
    
def parse_instructions(instruction):
    return re.findall(r'\w+', instruction)

def get_answer(filename='input.txt'):
    directions, m = parse_input('2023/8/'+filename)
    node = 'AAA'
    steps = 0
    while node != 'ZZZ':
        node = m[node][int(directions[steps%len(directions)])]
        steps += 1
    
    return steps


answer = get_answer()#'test_input.txt')
print(answer)