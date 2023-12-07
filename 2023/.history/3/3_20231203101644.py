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

def get_number(line, index, found_indexes: set):
    if index in found_indexes:
        return 0
    number = line[index]
    #indexes = [index]
    found_indexes.add(index)
    #forwards
    while True:
        index += 1
        if index in found_indexes:
            return 0, []
        try:
            if line[index].isdigit():
                number += line[index]
                found_indexes.add(index)
            else:
                break
        except IndexError:
            break
    
    #backwards
    index = indexes[0]
    while True:
        index -= 1
        if index in found_indexes:
            return 0, []
        try:
            if line[index].isdigit():
                number = line[index] + number
                found_indexes.add(index)
            else:
                break
        except IndexError:
            break
    
    return int(number), indexes

def get_answer(lines, indexes):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1)]
    answer = 0
    found_indexes = set()
    for coord in indexes:
        for neighbor in neighbors:
            try:
                if lines[coord[0] + neighbor[0]][coord[1] + neighbor[1]].isdigit():
                    print(coord, neighbor, lines[coord[0] + neighbor[0]][coord[1] + neighbor[1]])
                    _answer, found_indexes = get_number(lines[coord[0] + neighbor[0]], coord[1] + neighbor[1], found_indexes)
                    print(_answer, found_indexes)
                    answer += _answer
                    #found_indexes.update(_found_indexes)
            except IndexError:
                continue
    
    return answer
        





lines = parse_input('test_input.txt')
print(lines)
indexes = get_symbol_indexes(lines)
print(indexes)
answer = get_answer(lines, indexes)
print(answer)