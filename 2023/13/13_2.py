from copy import deepcopy

transpose = lambda x: [list(y) for y in zip(*x)]
flip = lambda x: '.' if x == '#' else '#'

def backtrack(grid, idx):
    for i in range(0,min(idx+1, len(grid)-idx-1)):
        if grid[idx-i] != grid[idx+1+i]:
            return False
    return True

def get_mirror(grid, orientation=None, existing_mirror=None):
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:
            if backtrack(grid,i):
                if (i,orientation) != existing_mirror:
                    return i

def check_possibilities(grid, existing_mirror):
    for i,line in enumerate(grid):
        for j in range(len(line)):
            _grid = deepcopy(grid)
            #print(_grid[i][j], _grid[i])
            _grid[i][j] = flip(_grid[i][j])
            v = get_mirror(_grid, 0, existing_mirror)
            if v is not None:
                return (v+1)*100
            __grid = transpose(_grid)
            v = get_mirror(__grid, 1, existing_mirror)
            if v is not None:
                return v+1

def calculate(grid):
    e = get_mirror(grid)
    if e is None:
        _grid = transpose(grid)
        existing_mirror = (get_mirror(_grid), 1)
    else:
        existing_mirror = (e,0)
    return check_possibilities(grid, existing_mirror)

def get_answer(filename='input.txt'):
    total = 0
    lines = []
    for line in open('2023/13/'+filename, 'r'):
        if line == '\n':
            total += calculate(lines)
            lines = []
        else:
            lines.append(list(line.rstrip('\n')))
    total += calculate(lines)
    return total

answer = get_answer()#'test_input.txt')
print(answer)