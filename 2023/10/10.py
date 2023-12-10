def parse_input(filename):
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]

def follow_paths(lines, start, second_node):

    steps = 1
    current = second_node
    prev = start
    while True:
        _c = current
        current = get_next_move(lines, current, prev)
        steps += 1
        if current == start:
            return steps
        else:
            prev = _c

def get_first_move(lines, start):
    if start[1]+1 < len(lines[start[0]]):
        if lines[start[0]][start[1]+1] in '-J7':
            return (start[0],start[1]+1)
    
    if start[1]-1 >= 0:
        if lines[start[0]][start[1]-1] in '-FL':
            return (start[0],start[1]-1)
    
    if start[0]+1 < len(lines):
        if lines[start[0]+1][start[1]] in '|F7':
            return (start[0]+1,start[1])

    if start[0]-1 >= 0:
        if lines[start[0]-1][start[1]] in '|JL':
            return (start[0]-1,start[1])
    
    return None

def get_next_move(lines, current, prev):
    if current[1]+1 < len(lines[current[0]]) and prev != (current[0],current[1]+1) and lines[current[0]][current[1]] in '-FLS':
        if lines[current[0]][current[1]+1] in '-J7S':
            return (current[0],current[1]+1)
    
    if current[1]-1 >= 0 and prev != (current[0],current[1]-1) and lines[current[0]][current[1]] in '-J7S':
        if lines[current[0]][current[1]-1] in '-FLS':
            return (current[0],current[1]-1)
    
    if current[0]+1 < len(lines) and prev != (current[0]+1,current[1]) and lines[current[0]][current[1]] in '|F7S':
        if lines[current[0]+1][current[1]] in '|JLS':
            return (current[0]+1,current[1])

    if current[0]-1 >= 0 and prev != (current[0]-1,current[1]) and lines[current[0]][current[1]] in '|JLS':
        if lines[current[0]-1][current[1]] in '|F7S':
            return (current[0]-1,current[1])


def get_answer(filename='input.txt'):
    lines = parse_input('2023/10/'+filename)
    start = next((i, j) for i, row in enumerate(lines) for j, item in enumerate(row) if item == 'S')

    next_node = get_first_move(lines, start)
    path_length = follow_paths(lines, start, next_node)
    answer = path_length//2

    return answer

answer = get_answer('test_input.txt')
print(answer)