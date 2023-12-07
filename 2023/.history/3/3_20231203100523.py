import re

def parse_input(filename='input.txt'):
    with open('3/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    return lines

def get_symbol_indexes(lines):
    symbols = '#*$-%+@=&/'
    coordinates = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in symbols:
                coordinates.append((i, j))

    return coordinates

def get_number(line):


def get_answer(lines, indexes):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1)]
    answer = 0
    
    for coord in indexes:
        for neighbor in neighbors:
            try:
                if lines[coord[0] + neighbor[0]][coord[1] + neighbor[1]].isdigit():
                    answer += get_number(lines[coord[0] + neighbor[0]])
            
            except IndexError:
                continue
        





lines = parse_input('test_input.txt')
print(lines)
indexes = get_symbol_indexes(lines)
print(indexes)