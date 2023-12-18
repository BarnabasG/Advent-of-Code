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

def parse_input(filename):
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]

def run(lines, beams=[(0,0,Dir.RIGHT)], visited={(0,0)}, visited_with_dir={(0,0,Dir.RIGHT)}):
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
    return run(lines, _beams, visited)                


def get_answer(filename='input.txt'):
    lines = parse_input('2023/16/'+filename)
    answer = run(lines)
    return answer

answer = get_answer()#'test_input.txt')
print(answer)