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
    
    MAX_X = 101
    MAX_Y = 103

    for _ in range(100):
        for robot in robots:
            robot[0] = ((robot[0][0] + robot[1][0]) % MAX_X, (robot[0][1] + robot[1][1]) % MAX_Y)
    
    # [print(r[0]) for r in robots]

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
    

def treelike(robots):
    """Look on the 2d 101*103 grid for the shape:
    ..#..
    .###.
    #####
    """
    rows = {row: [coord for (coord), _ in robots if coord[1] == row] for row in set(coord[1] for coord in (coord), _ in robots)}

        


def p2(filename):
    robots = []
    for line in read_gen(filename):
        # print(line)
        px, py, vx, vy = map(int, re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line).groups())
        robots.append([(px, py), (vx, vy)])
    
    MAX_X = 101
    MAX_Y = 103

    while not treelike(robots):
        for robot in robots:
            robot[0] = ((robot[0][0] + robot[1][0]) % MAX_X, (robot[0][1] + robot[1][1]) % MAX_Y)
    
    # [print(r[0]) for r in robots]

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


print(p1('2024/14/input.txt'))
# print(p2('2024/12/test_input.txt'))

# from pybencher import Suite

# filename = '2024/12/input.txt'
# suite = Suite()
# suite.add(p1, filename)
# suite.run()
