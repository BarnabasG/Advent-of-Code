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
        print(current, steps)
        if current == start:
            return steps
        else:
            prev = _c

def get_loop(lines, start, second_node):
    current = second_node
    prev = start
    loop_cells = set()
    while True:
        _c = current
        current = get_next_move(lines, current, prev)
        loop_cells.add(current)
        if current == start:
            return loop_cells
        else:
            prev = _c

def get_start_char(exits: dict):
    if set(exits.keys()) == {'-', '|'}:
        if exits['-'] == (0,1):
            if exits['|'] == (-1,0):
                return 'L'
            elif exits['|'] == (1,0):
                return 'F'
        elif exits['-'] == (0,-1):
            if exits['|'] == (-1,0):
                return 'J'
            elif exits['|'] == (1,0):
                return '7'
    elif '-' in exits:
        return '-'
    elif '|' in exits:
        return '|'

def get_first_move(lines, start):
    exits = []
    if start[1]+1 < len(lines[start[0]]):
        if lines[start[0]][start[1]+1] in '-J7':
            exits.append((start[0],start[1]+1))
    
    if start[1]-1 >= 0:
        if lines[start[0]][start[1]-1] in '-FL':
            exits.append((start[0],start[1]-1))
    
    if start[0]+1 < len(lines):
        if lines[start[0]+1][start[1]] in '|F7':
            exits.append((start[0]+1,start[1]))

    if start[0]-1 >= 0:
        if lines[start[0]-1][start[1]] in '|JL':
            exits.append((start[0]-1,start[1]))
    
    return exits

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

def get_inside_loop(lines, loop):
    inside_count = 0
    for i, line in enumerate(lines):
        inside = False
        last = None
        for j, char in enumerate(line):
            if not inside and (i,j) not in loop:
                continue
            elif (i,j) in loop:
                if char == '|':
                    inside = not inside
                elif char == 'J':
                    if last == 'F':
                        inside = not inside
                    last = None
                elif char == '7':
                    if last == 'L':
                        inside = not inside
                    last = None
                elif char == 'L':
                    last = 'L'
                elif char == 'F':
                    last = 'F'
            elif (i,j) not in loop:
                if inside:
                    inside_count += 1
                last = None
    return inside_count

def get_answer(filename='input.txt'):
    lines = parse_input('2023/10/'+filename)
    start = next((i, j) for i, row in enumerate(lines) for j, item in enumerate(row) if item == 'S')
    routes = get_first_move(lines, start)
    next_node = routes[0]
    loop = get_loop(lines, start, next_node)
    exits = {lines[v[0]][v[1]]:(v[0]-start[0],v[1]-start[1]) for v in routes}
    lines[start[0]][start[1]] = get_start_char(exits)
    answer = get_inside_loop(lines, loop)

    return answer

answer = get_answer()#'test_input.txt')
print(answer)