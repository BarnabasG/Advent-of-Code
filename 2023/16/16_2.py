from enum import Enum
class Dir(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

mapping = {
    (Dir.RIGHT, '\\'): [Dir.DOWN],
    (Dir.RIGHT, '/'): [Dir.UP],
    (Dir.RIGHT, '-'): [Dir.RIGHT],
    (Dir.RIGHT, '|'): [Dir.UP, Dir.DOWN],
    (Dir.LEFT, '\\'): [Dir.UP],
    (Dir.LEFT, '/'): [Dir.DOWN],
    (Dir.LEFT, '-'): [Dir.LEFT],
    (Dir.LEFT, '|'): [Dir.UP, Dir.DOWN],
    (Dir.UP, '\\'): [Dir.LEFT],
    (Dir.UP, '/'): [Dir.RIGHT],
    (Dir.UP, '-'): [Dir.LEFT, Dir.RIGHT],
    (Dir.UP, '|'): [Dir.UP],
    (Dir.DOWN, '\\'): [Dir.RIGHT],
    (Dir.DOWN, '/'): [Dir.LEFT],
    (Dir.DOWN, '-'): [Dir.LEFT, Dir.RIGHT],
    (Dir.DOWN, '|'): [Dir.DOWN],
}

import sys
print(sys.getrecursionlimit())

def parse_input(filename):
    with open(filename, 'r') as f:
        return tuple(list(line.rstrip('\n')) for line in f.readlines())

from functools import cache

@cache
def simulate(lines, beams=((0,0,Dir.RIGHT)), visited={(0,0)}, visited_with_dir={(0,0,Dir.RIGHT)}):
    _beams = []
    for b in beams:
        visited.add((b[0], b[1]))
        visited_with_dir.add(b)
        if lines[b[0]][b[1]] == '.':
            if 0 <= b[0]+b[2].value[0] < len(lines) and 0 <= b[1]+b[2].value[1] < len(lines[0]) and (b[0]+b[2].value[0], b[1]+b[2].value[1], b[2]) not in visited_with_dir:
                _beams.append((b[0]+b[2].value[0], b[1]+b[2].value[1], b[2]))
        elif lines[b[0]][b[1]] in '|-/\\':
            for d in mapping[(b[2], lines[b[0]][b[1]])]:
                if 0 <= b[0]+d.value[0] < len(lines) and 0 <= b[1]+d.value[1] < len(lines[0]) and (b[0]+d.value[0], b[1]+d.value[1], d) not in visited_with_dir:
                    _beams.append((b[0]+d.value[0], b[1]+d.value[1], d))

    if len(_beams) == 0:
        return len(visited)
    return simulate(lines, tuple(_beams), visited, visited_with_dir)

def run(lines):
    maximum = 0
    for i in range(len(lines)):
        s = simulate(lines, beams=((i,0,Dir.RIGHT)), visited={(i,0)}, visited_with_dir={(i,0,Dir.RIGHT)})
        if s > maximum:
            maximum = s
        s = simulate(lines, beams=((i,len(lines[0])-1,Dir.LEFT)), visited={(i,len(lines[0])-1)}, visited_with_dir={(i,len(lines[0])-1,Dir.LEFT)})
        if s > maximum:
            maximum = s
    for i in range(len(lines[0])):
        s = simulate(lines, beams=((0,i,Dir.DOWN)), visited={(0,i)}, visited_with_dir={(0,i,Dir.DOWN)})
        if s > maximum:
            maximum = s
        s = simulate(lines, beams=((len(lines)-1,i,Dir.UP)), visited={(len(lines)-1,i)}, visited_with_dir={(len(lines)-1,i,Dir.UP)})
        if s > maximum:
            maximum = s

    return maximum

def get_answer(filename='input.txt'):
    lines = parse_input('2023/16/'+filename)
    sys.setrecursionlimit(len(lines) * len(lines[0]))
    print(sys.getrecursionlimit())
    answer = run(lines)
    return answer

answer = get_answer()#'test_input.txt')
print(answer)