import re

def parse_input(filename='input.txt'):
    with open('2023/2/'+filename, 'r') as f:
        lines = [parse_line(line.rstrip('\n')) for line in f.readlines()]
    return lines

def parse_line(line):
    game = int(re.search(r'Game (\d+):', line).group(1))
    max_blue = max(map(int, re.findall(r'(\d+) blue', line)))
    max_red = max(map(int, re.findall(r'(\d+) red', line)))
    max_green = max(map(int, re.findall(r'(\d+) green', line)))
    return game, max_blue, max_red, max_green

def get_answer(lines):
    valid = 0
    red_max, green_max, blue_max = 12, 13, 14
    for line in lines:
        number, blue, red, green = line
        if blue > blue_max or red > red_max or green > green_max:
            continue
        valid += number
    return valid
        

lines = parse_input()#'test_input.txt')
answer = get_answer(lines)
print(answer)