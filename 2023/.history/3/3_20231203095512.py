import re

def parse_input(filename='input.txt'):
    with open('3/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    return lines

def get_symbol_indexes(lines):
    symbols = '#*$-%+@=&/'.split()
    for line in lines:
        symbols.append(line.find('#'))
    



lines = parse_input('test_input.txt')
print(lines)