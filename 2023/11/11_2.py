from itertools import combinations

def parse_input(filename):
    with open(filename, 'r') as f:
        return [line.rstrip('\n') for line in f.readlines()]

def get_answer(filename='input.txt'):
    lines = parse_input('2023/11/'+filename)
    empty_rows, empty_cols = [i for i,line in enumerate(lines) if '#' not in line], [x for x,line in enumerate(list(zip(*lines))) if '#' not in line]
    coords = [(i,j) for i,line in enumerate(lines) for j,char in enumerate(line) if char == '#']
    coords = ((c[0]+999_999*sum(x<c[0] for x in empty_rows),c[1]+999_999*sum(x<c[1] for x in empty_cols)) for c in coords)
    return sum([abs(c1[0]-c2[0])+abs(c1[1]-c2[1]) for c1,c2 in combinations(coords,2)])

answer = get_answer()#'test_input.txt')
print(answer)