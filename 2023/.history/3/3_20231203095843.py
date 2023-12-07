import re

def parse_input(filename='input.txt'):
    with open('3/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    return lines

def get_symbol_indexes(lines):
    symbols = '#*$-%+@=&/'.split()
    coordinates = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in symbols:
                coordinates.append((i, j))

    return coordinates
    



lines = parse_input('test_input.txt')
print(lines)
indexes = get_symbol_indexes(lines)
print(indexes)