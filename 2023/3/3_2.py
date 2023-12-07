import numpy

def parse_input(filename='input.txt'):
    with open('2023/3/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    return lines

def get_symbol_indexes(lines):
    symbols = '*'
    coordinates = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in symbols:
                coordinates.append((i, j))

    return coordinates

def get_number(line, line_index, index, found_indexes: set):
    if (line_index, index) in found_indexes:
        return -1, found_indexes
    number = line[index]
    found_indexes.add((line_index, index))
    _index = index

    #forwards
    while True:
        index += 1
        if index in found_indexes:
            return -1, found_indexes
        try:
            if line[index].isdigit():
                number += line[index]
                found_indexes.add((line_index, index))
            else:
                break
        except IndexError:
            break
    
    #backwards
    index = _index
    while True:
        index -= 1
        if index in found_indexes:
            return -1, found_indexes
        try:
            if line[index].isdigit():
                number = line[index] + number
                found_indexes.add((line_index, index))
            else:
                break
        except IndexError:
            break
    
    return int(number), found_indexes

def get_answer(lines, indexes):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1)]
    answer = 0
    found_neighbors = []
    for coord in indexes:
        found_neighbors.append([])
        found_indexes = set()
        for neighbor in neighbors:
            try:
                if lines[coord[0] + neighbor[0]][coord[1] + neighbor[1]].isdigit():
                    _answer, found_indexes = get_number(lines[coord[0] + neighbor[0]], coord[0] + neighbor[0], coord[1] + neighbor[1], found_indexes)
                    if _answer == -1: continue
                    found_neighbors[-1].append(_answer)
            except IndexError:
                continue
    for found_neighbor in found_neighbors:
        if len(found_neighbor) == 2:
            answer += numpy.prod(found_neighbor)
    
    return answer

lines = parse_input()#'test_input.txt')
indexes = get_symbol_indexes(lines)
answer = get_answer(lines, indexes)
print(answer)