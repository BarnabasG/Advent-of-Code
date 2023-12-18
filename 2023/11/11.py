from itertools import combinations

def parse_input(filename):
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]

def expand_empty(lines):
    [lines.insert(r,['.']*len(lines[0])) for r in [i for i,line in enumerate(lines) if '#' not in line][::-1]]
    [lines[x].insert(c,'.') for c in [x for x,line in enumerate(list(zip(*lines))) if '#' not in line][::-1] for x in range(len(lines))]
    return lines

def get_distances(lines):
    coords = [(i,j) for i,line in enumerate(lines) for j,char in enumerate(line) if char == '#']
    return sum([abs(c1[0]-c2[0])+abs(c1[1]-c2[1]) for c1,c2 in combinations(coords,2)])

def get_answer(filename='input.txt'):
    lines = expand_empty(parse_input('2023/11/'+filename))
    return get_distances(lines)

answer = get_answer()#'test_input.txt')
print(answer)