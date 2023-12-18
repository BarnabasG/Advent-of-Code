import re

mapping = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0),
}

def print_grid(grid, coord=None):
    for i in range(min(x[0] for x in grid),max([x[0] for x in grid])+1):
        for j in range(min(x[1] for x in grid),max([x[1] for x in grid])+1):
            if (i,j) == coord:
                print('X', end='')
            elif (i,j) in grid:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

def parse_input(filename):
    def parse(line):
        return (line[0], int(re.search(r'\d+', line).group(0)), re.search(r'\((.*)\)', line).group(0))
    with open(filename, 'r') as f:
        return [parse(line.rstrip('\n')) for line in f.readlines()]

def dig(instructions):
    c = (0,0)
    visited = {c}
    for instruct in instructions:
        for _ in range(instruct[1]):
            c = (c[0]+mapping[instruct[0]][0], c[1]+mapping[instruct[0]][1])
            visited.add(c)
    return visited

def fill(visited):
    # flood fill
    min_y = min(x[0] for x in visited)
    min_x = min(x[1] for x in visited if x[0] == min_y)
    start = (min_y+1, min_x+1)
    stack = [start]
    while stack:
        y, x = stack.pop()
        if (y, x) not in visited:
            visited.add((y, x))
            stack.extend([(y+1, x), (y-1, x), (y, x+1), (y, x-1)])

    return visited

def get_answer(filename='input.txt'):
    lines = parse_input('2023/18/'+filename)
    v = fill(dig(lines))
    return len(v)

answer = get_answer()#'test_input.txt')
print(answer)