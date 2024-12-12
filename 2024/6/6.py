def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def p1(filename):
    lines = read_lines(filename)
    obstables = set()
    guard = None
    guard_directions = {
        '^': (-1, 0, '>'),
        '>': (0, 1, 'v'),
        'v': (1, 0, '<'),
        '<': (0, -1, '^')
    }
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            match lines[i][j]:
                case '#':
                    obstables.add((i, j))
                case '^':
                    guard = [i, j, '^']
    
    visited = {(guard[0], guard[1])}

    while True: 
        if (guard[0] + guard_directions[guard[2]][0], guard[1] + guard_directions[guard[2]][1]) in obstables:
            guard[2] = guard_directions[guard[2]][2]
        else:
            guard[0] += guard_directions[guard[2]][0]
            guard[1] += guard_directions[guard[2]][1]
            if not (0 <= guard[0] <= len(lines) and 0 <= guard[1] <= len(lines[0])):
                break
            visited.add((guard[0], guard[1]))

    return len(visited) - 1

def p2(filename):
    lines = read_lines(filename)
    obstables = set()
    direction = '^'
    guard_directions = {
        '^': (-1, 0, '>'),
        '>': (0, 1, 'v'),
        'v': (1, 0, '<'),
        '<': (0, -1, '^')
    }
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            match lines[i][j]:
                case '#':
                    obstables.add((i, j))
                case '^':
                    guard_initial = (i, j)
    
    guard = guard_initial
    original_path = set()
    while True: 
        if (guard[0] + guard_directions[direction][0], guard[1] + guard_directions[direction][1]) in obstables:
            direction = guard_directions[direction][2]
        else:
            guard = (guard[0] + guard_directions[direction][0], guard[1] + guard_directions[direction][1])
            if not (0 <= guard[0] <= len(lines) and 0 <= guard[1] <= len(lines[0])):
                break
            elif (guard, direction) in original_path:
                cycles += 1
                break
            original_path.add(guard)
    
    cycles = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not (i,j) in original_path:
                continue
            obstacles_new = set(obstables)
            obstacles_new.add((i, j))
            guard = guard_initial
            direction = '^'
            visited = {(guard, direction)}

            while True:
                if (guard[0] + guard_directions[direction][0], guard[1] + guard_directions[direction][1]) in obstacles_new:
                    direction = guard_directions[direction][2]
                else:
                    guard = (guard[0] + guard_directions[direction][0], guard[1] + guard_directions[direction][1])
                    if not (0 <= guard[0] <= len(lines) and 0 <= guard[1] <= len(lines[0])):
                        break
                    elif (guard, direction) in visited:
                        cycles += 1
                        break
                    visited.add((guard, direction))

    return cycles

def p2_2(filename):
    lines = read_lines(filename)
    obstacles = set()
    direction = '^'
    guard_directions = {
        '^': (-1, 0, '>'),
        '>': (0, 1, 'v'),
        'v': (1, 0, '<'),
        '<': (0, -1, '^')
    }
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            match lines[i][j]:
                case '#':
                    obstacles.add((i, j))
                case '^':
                    guard_initial = (i, j)
    
    guard = guard_initial
    original_path = set()
    original_directions = {}
    while True:
        next_pos = (guard[0] + guard_directions[direction][0], guard[1] + guard_directions[direction][1])
        if next_pos in obstacles:
            direction = guard_directions[direction][2]
        else:
            guard = next_pos
            if not (0 <= guard[0] < len(lines) and 0 <= guard[1] < len(lines[0])):
                break
            if (guard, direction) in original_path:
                # Original path doesn't cycle
                return 0
            original_path.add((guard, direction))
            original_directions[guard] = direction
    
    print(original_directions)

    cycles = 0
    for pos in original_directions:
        obstacles_new = set(obstacles)
        obstacles_new.add(pos)

        guard = guard_initial
        direction = '^'
        visited = set()
        while True:
            next_pos = (guard[0] + guard_directions[direction][0], guard[1] + guard_directions[direction][1])
            if next_pos in obstacles_new:
                direction = guard_directions[direction][2]
            else:
                guard = next_pos
                if not (0 <= guard[0] < len(lines) and 0 <= guard[1] < len(lines[0])):
                    break
                if (guard, direction) in visited:
                    cycles += 1
                    break
                visited.add((guard, direction))

    return cycles



from pybencher import Suite

s = Suite()

s.add(p1, '2024/6/input.txt')
s.add(p2, '2024/6/input.txt')
s.add(p2_2, '2024/6/input.txt')

s.verbose = True
# s.run()


# print(p1('2024/6/input.txt'))
print(p2_2('2024/6/input.txt'))