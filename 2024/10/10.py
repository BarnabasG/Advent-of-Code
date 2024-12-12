def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def search(lines, i, j, number, visited):
    if number == 9:
        return {(i, j)}
    visited.add((i, j))
    reachable = set()
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = i + di, j + dj
        if (
            0 <= ni < len(lines) and 0 <= nj < len(lines[0]) and
            lines[ni][nj] == number + 1 and (ni, nj) not in visited
        ):
            reachable.update(search(lines, ni, nj, number + 1, visited))
    visited.remove((i, j))
    return reachable

def search_2(lines, i, j, number):
    if number == 9:
        return 1
    trails = 0
    for move in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = i + move[0], j + move[1]
        if 0 <= ni < len(lines) and 0 <= nj < len(lines[0]) and lines[ni][nj] == number + 1:
            trails += search_2(lines, i + move[0], j + move[1], number+1)
    return trails

def p1(filename):
    lines = [list(map(int, line)) for line in read_lines(filename)]
    trailheads = [(i, j) for i, row in enumerate(lines) for j, val in enumerate(row) if val == 0]
    trails = sum(len(search(lines, x, y, 0, set())) for x, y in trailheads)
    
    return trails



def p2(filename):
    lines = [list(map(int, line)) for line in read_lines(filename)]
    trailheads = [(i, j) for i, row in enumerate(lines) for j, val in enumerate(row) if val == 0]
    trails = sum(search_2(lines, x, y, 0) for x, y in trailheads)
    
    return trails


print(p1('2024/10/input.txt'))
print(p2('2024/10/input.txt'))

filename = '2024/10/input.txt'

from pybencher import Suite

suite = Suite()

suite.add(p1, filename)
suite.add(p2, filename)

suite.run()