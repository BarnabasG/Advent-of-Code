import re

def parse_input(filename='input.txt'):
    with open('2/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [parse_line(line.rstrip('\n')) for line in lines]
    print(lines)
    return lines

def parse_line(line):
    game = int(re.search(r'Game (\d+):', line).group(1))
    print(game)

def get_answer(lines):
    valid = 0
    for line in lines:
        pass
        


lines = parse_input('test_input.txt')
answer = get_answer(lines)