import re

def parse_input(filename='input.txt'):
    with open('2/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [parse_line(line.rstrip('\n')) for line in lines]
    print(lines)
    return lines

def parse_line(line):
    game = int(re.search(r'Game (\d+):', line).group(1))
    max_blue = max(map(int, re.findall(r'(\d+) blue', line)))
    max_red = max(map(int, re.findall(r'(\d+) red', line)))
    max_green = max(map(int, re.findall(r'(\d+) green', line)))
    return game, max_blue, max_red, max_green

def get_answer(lines):
    valid = 0
    power = lambda x,y,z: x*y*z
    for line in lines:
        _, blue, red, green = line
        valid += power(blue, red, green)
    return valid
        

lines = parse_input('test_input.txt')
answer = get_answer(lines)
print(answer)