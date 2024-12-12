from itertools import combinations


def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def print_map(max_x, max_y, antinodes):
    for i in range(max_x):
        for j in range(max_y):
            if (i, j) in antinodes:
                print('X', end='')
            else:
                print('.', end='')
        print()


def p1(filename):
    lines = read_lines(filename)
    nodes = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.':
                nodes.setdefault(lines[i][j], []).append((i, j))

    antinodes = set()
    max_x, max_y = len(lines), len(lines[0])
    for locs in nodes.values():
        for pair in combinations(locs, 2):
            dx,  dy = pair[1][0] - pair[0][0], pair[1][1] - pair[0][1]
            a1 = (pair[0][0] - dx, pair[0][1] - dy)
            a2 = (pair[1][0] + dx, pair[1][1] + dy)
            if 0 <= a1[0] < max_x and 0 <= a1[1] < max_y:
                antinodes.add(a1)
            if 0 <= a2[0] < max_x and 0 <= a2[1] < max_y:
                antinodes.add(a2)
    # print_map(max_x, max_y, antinodes)
    return len(antinodes)

def p2(filename):
    lines = read_lines(filename)
    nodes = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '.':
                nodes.setdefault(lines[i][j], []).append((i, j))

    antinodes = set()
    max_x, max_y = len(lines), len(lines[0])
    for locs in nodes.values():
        for pair in combinations(locs, 2):
            dx,  dy = pair[1][0] - pair[0][0], pair[1][1] - pair[0][1]
            pos = (pair[0][0] + dx, pair[0][1] + dy)
            while 0 <= pos[0] < max_x and 0 <= pos[1] < max_y:
                antinodes.add(pos)
                pos = (pos[0] + dx, pos[1] + dy)
            
            pos = (pair[1][0] - dx, pair[1][1] - dy)
            while 0 <= pos[0] < max_x and 0 <= pos[1] < max_y:
                antinodes.add(pos)
                pos = (pos[0] - dx, pos[1] - dy)
    # print_map(max_x, max_y, antinodes)

    return len(antinodes)

filename = '2024/8/input.txt'
print(p1(filename))
print(p2(filename))

from pybencher import Suite

suite = Suite()
suite.add(p1, filename)
suite.add(p2, filename)

suite.run()