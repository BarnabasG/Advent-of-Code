from collections import deque
import heapq


def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def bfs(start, end, walls):
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    best_path = (None, float('inf'))
    queue = deque([([start], (0,1), 0)])

    score_dict = {}
    
    while queue:
        path, prev_dir, score = queue.popleft()
        current = path[-1]

        if current == end:
            if best_path is None or score < best_path[1]:
                best_path = (path, score)
            continue
        
        for current_dir in DIRECTIONS:
            next_pos = (current[0] + current_dir[0], current[1] + current_dir[1])
            
            if (next_pos in walls or next_pos in path):
                continue
            
            if current_dir == prev_dir:
                s = 1
            else:
                s = 1001 if prev_dir[0] * current_dir[1] - prev_dir[1] * current_dir[0] != 0 else -1
            
            if s == -1:
                continue

            if score + s > best_path[1]:
                continue

            if (current_dir, next_pos) in score_dict and score + s >= score_dict[(current_dir, next_pos)]:
                continue

            score_dict[(current_dir, next_pos)] = score + s
            
            queue.append((
                path + [next_pos], 
                current_dir, 
                score + s
            ))

    return best_path[1]

def bfs_2(start, end, walls):
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    best_paths = set()
    best_score = float('inf')
    queue = deque([([start], (0,1), 0)])

    score_dict = {}
    
    while queue:
        path, prev_dir, score = queue.popleft()
        current = path[-1]

        if current == end:
            if score < best_score:
                best_paths = set(path)
                best_score = score
            elif score == best_score:
                best_paths |= set(path)
            continue
        
        for current_dir in DIRECTIONS:
            next_pos = (current[0] + current_dir[0], current[1] + current_dir[1])
            
            if (next_pos in walls or next_pos in path):
                continue

            s = 1 if prev_dir == current_dir else 1001 if prev_dir[0] * current_dir[1] - prev_dir[1] * current_dir[0] != 0 else -1
            
            if s == -1:
                continue

            if score + s > best_score:
                continue

            if (current_dir, next_pos) in score_dict and score + s > score_dict[(current_dir, next_pos)]:
                continue

            score_dict[(current_dir, next_pos)] = score + s
            
            queue.append((
                path + [next_pos], 
                current_dir, 
                score + s
            ))
    
    # print('best score', best_score)
    # draw(best_paths, walls)

    return best_paths



def draw(path, walls):
    for i in range(max(x for x, _ in walls) + 1):
        for j in range(max(y for _, y in walls) + 1):
            if (i, j) in walls:
                print('#', end='')
            elif (i, j) in path:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def p1(filename):
    lines = read_lines(filename)
    walls = set()
    start, end = None, None
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                walls.add((i, j))
            elif char == 'S':
                start = (i, j)
            elif char == 'E':
                end = (i, j)
    
    return bfs(start, end, walls)
        

def p2(filename):
    lines = read_lines(filename)
    walls = set()
    start, end = None, None
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                walls.add((i, j))
            elif char == 'S':
                start = (i, j)
            elif char == 'E':
                end = (i, j)
    
    return len(bfs_2(start, end, walls))


# print(p1('2024/16/input.txt'))
# print(p2('2024/16/input.txt'))

from pybencher import Suite

suite = Suite()

filename = '2024/16/test_input.txt'
suite.add(p1, filename)
suite.add(p2, filename)

suite.run()