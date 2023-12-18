transpose = lambda x: list(zip(*x))

def backtrack(grid, idx):
    for i in range(1,min(idx+1, len(grid)-idx-1)):
        if grid[idx-i] != grid[idx+1+i]:
            return False
    return True

def validate(grid, m):
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:
            if backtrack(grid,i): return m*(i+1)

def calculate(grid):
    v = validate(grid, 100)
    if v: return v
    grid = transpose(grid)
    v = validate(grid, 1)
    if v: return v

def get_answer(filename='input.txt'):
    total = 0
    lines = []
    for line in open('2023/13/'+filename, 'r'):
        if line == '\n':
            total += calculate(lines)
            lines = []
        else:
            lines.append(line.rstrip('\n'))
    total += calculate(lines)
    return total

answer = get_answer()#'test_input.txt')
print(answer)