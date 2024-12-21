from functools import cache

def read_lines(filename):
    return [line.rstrip('\n') for line in open(filename)]

KEYPAD_GRID = ["789", "456", "123", " 0A"]
REMOTE_GRID = [" ^A", "<v>"]

def find_pos(grid, char):
    return next((x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == char)

def find_optimal_path(grid, from_char, to_char):
    start_x, start_y = find_pos(grid, from_char)
    target_x, target_y = find_pos(grid, to_char)
    
    def generate_paths(x, y, path=""):
        if (x, y) == (target_x, target_y):
            yield path + 'A'
            return
            
        moves = [
            (x > 0 and target_x < x and grid[y][x-1] != ' ', x-1, y, '<'),
            (y > 0 and target_y < y and grid[y-1][x] != ' ', x, y-1, '^'),
            (y < len(grid)-1 and target_y > y and grid[y+1][x] != ' ', x, y+1, 'v'),
            (x < len(grid[0])-1 and target_x > x and grid[y][x+1] != ' ', x+1, y, '>')
        ]
        
        for valid, new_x, new_y, direction in moves:
            if valid:
                yield from generate_paths(new_x, new_y, path + direction)
    
    def count_direction_changes(path):
        return sum(a != b for a, b in zip(path, path[1:]))
    
    return min(generate_paths(start_x, start_y), key=count_direction_changes)

@cache
def solve_recur(sequence, level, robots):
    if level > robots:
        return len(sequence)
    
    grid = REMOTE_GRID if level > 0 else KEYPAD_GRID
    return sum(solve_recur(find_optimal_path(grid, start, end), level + 1, robots) for start, end in zip('A' + sequence, sequence))

def p1(filename):
    return sum(solve_recur(s, 0, 2) * int(s[:3]) for s in read_lines(filename))

def p2(filename):
    return sum(solve_recur(s, 0, 25) * int(s[:3]) for s in read_lines(filename))

print(p1('2024/21/input.txt'))
print(p2('2024/21/input.txt'))

from pybencher import Suite

suite = Suite()
filename = '2024/21/input.txt'

suite.add(p1, filename)
suite.add(p2, filename)

suite.run()