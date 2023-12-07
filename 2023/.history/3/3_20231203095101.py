import re

def parse_input(filename='input.txt'):
    with open('3/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    print(lines)
    return lines



lines = parse_input('test_input.txt')
print(lines)