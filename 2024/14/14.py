import re


def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def p1(filename):
    robots = []
    for line in read_gen(filename):
        # print(line)
        px, py, vx, vy = map(int, re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line).groups())
        robots.append([(px, py), (vx, vy)])
    
    MAX_X = 11
    MAX_Y = 7

    for _ in range(100):
        for robot in robots:
            robot[0] = ((robot[0][0] + robot[1][0]) % MAX_X, (robot[0][1] + robot[1][1]) % MAX_Y)
    
    # [print(r[0]) for r in robots]
    
    # draw([r[0] for r in robots], MAX_X, MAX_Y)

    # qs = [[],[],[],[]]
    q1, q2, q3, q4 = 0, 0, 0, 0
    # print(MAX_X//2, MAX_Y//2)
    for robot in robots:
        if robot[0][0] < MAX_X//2 and robot[0][1] < MAX_Y//2:
            # qs[0].append(robot)
            q1 += 1
        elif robot[0][0] > MAX_X//2 and robot[0][1] < MAX_Y//2:
            # qs[1].append(robot)
            q2 += 1
        elif robot[0][0] < MAX_X//2 and robot[0][1] > MAX_Y//2:
            # qs[2].append(robot)
            q3 += 1
        elif robot[0][0] > MAX_X//2 and robot[0][1] > MAX_Y//2:
            # qs[3].append(robot)
            q4 += 1
    # print(q1, q2, q3, q4)
    return q1*q2*q3*q4
    

def expand(centre_x, current_layer, all_positions, depth, required_depth):
    if depth == required_depth:
        return True
    next_layer = [(centre_x+i, p[1]+1) for i in range(-depth, depth+1) for p in current_layer]
    if not all(p in all_positions for p in next_layer):
        return False
    return expand(centre_x, next_layer, all_positions, depth+1, required_depth)

def treelike(positions):
    """
    ..#..
    .###.
    #####
    """
    for pos in positions:
        if expand(pos[0], [pos], positions, 1, 3):
            return True

    return False
        
def draw(positions, MAX_X, MAX_Y):
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if (x, y) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def p2(filename):
    robots = []
    for line in read_gen(filename):
        # print(line)
        px, py, vx, vy = map(int, re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line).groups())
        robots.append([(px, py), (vx, vy)])
    
    MAX_X = 101
    MAX_Y = 103

    seconds = 0
    while not treelike([r[0] for r in robots]):
        print(seconds)
        # draw([r[0] for r in robots], MAX_X, MAX_Y)
        for robot in robots:
            robot[0] = ((robot[0][0] + robot[1][0]) % MAX_X, (robot[0][1] + robot[1][1]) % MAX_Y)
        seconds += 1
        # if seconds > 99:
        #     break
    
    print(seconds)
    draw([r[0] for r in robots], MAX_X, MAX_Y)
    
    # print(robots)
    return seconds
    
    # [print(r[0]) for r in robots]

    # qs = [[],[],[],[]]
    # q1, q2, q3, q4 = 0, 0, 0, 0
    # # print(MAX_X//2, MAX_Y//2)
    # for robot in robots:
    #     if robot[0][0] < MAX_X//2 and robot[0][1] < MAX_Y//2:
    #         # qs[0].append(robot)
    #         q1 += 1
    #     elif robot[0][0] > MAX_X//2 and robot[0][1] < MAX_Y//2:
    #         # qs[1].append(robot)
    #         q2 += 1
    #     elif robot[0][0] < MAX_X//2 and robot[0][1] > MAX_Y//2:
    #         # qs[2].append(robot)
    #         q3 += 1
    #     elif robot[0][0] > MAX_X//2 and robot[0][1] > MAX_Y//2:
    #         # qs[3].append(robot)
    #         q4 += 1
    # # print(q1, q2, q3, q4)
    # return q1*q2*q3*q4


print(p1('2024/14/input.txt'))
print(p2('2024/14/input.txt'))

# from pybencher import Suite

# filename = '2024/12/input.txt'
# suite = Suite()
# suite.add(p1, filename)
# suite.run()
