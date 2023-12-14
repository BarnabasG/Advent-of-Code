def parse_input(filename):
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]

def get_rock_locations(lines):
    rocks, cubes = [], []
    for i, row in enumerate(lines):
        for j, item in enumerate(row):
            if item == 'O':
                rocks.append((i,j))
            elif item == '#':
                cubes.append((i,j))
    wall = [(-1, i) for i in range(len(lines[0]))] + [(len(lines), i) for i in range(len(lines[0]))] + [(i, -1) for i in range(len(lines))] + [(i, len(lines[0])) for i in range(len(lines))]
    return rocks, cubes, wall

def calculate_load(rocks,max_load):
    return sum([(max_load-rock[0]) for rock in rocks])

def spin(rocks, obstacle_set: set):

    rocks.sort(key=lambda x: x[0])
    for i, rock in enumerate(rocks):
        while (rock[0] - 1, rock[1]) not in obstacle_set:
            rock = (rock[0] - 1, rock[1])
        rocks[i] = rock
        obstacle_set.add(rock)

    rocks.sort(key=lambda x: x[1])
    for i, rock in enumerate(rocks):
        obstacle_set.remove(rock)
        while (rock[0], rock[1] - 1) not in obstacle_set:
            rock = (rock[0], rock[1] - 1)
        rocks[i] = rock
        obstacle_set.add(rock)

    rocks.sort(key=lambda x: x[0], reverse=True)
    for i, rock in enumerate(rocks):
        obstacle_set.remove(rock)
        while (rock[0] + 1, rock[1]) not in obstacle_set:
            rock = (rock[0] + 1, rock[1])
        rocks[i] = rock
        obstacle_set.add(rock)

    rocks.sort(key=lambda x: x[1], reverse=True)
    for i, rock in enumerate(rocks):
        obstacle_set.remove(rock)
        while (rock[0], rock[1] + 1) not in obstacle_set:
            rock = (rock[0], rock[1] + 1)
        rocks[i] = rock
        obstacle_set.add(rock)
        
    return rocks


def calculate(rocks, cubes, wall, height, times):
    cache_rocks = {tuple(rocks):0}
    cache_indices = {0:tuple(rocks)}
    for i in range(1,times+1):
        rocks = spin(rocks, set(cubes + wall))
        if tuple(rocks) in cache_rocks:
            loop_length = i - cache_rocks[tuple(rocks)]
            index = cache_rocks[tuple(rocks)] + (times-cache_rocks[tuple(rocks)]) % loop_length
            rocks = cache_indices[index]
            return calculate_load(rocks, height)
        else:
            cache_rocks[tuple(rocks)] = i
            cache_indices[i] = tuple(rocks)
    return rocks

def get_answer(filename='input.txt'):
    lines = parse_input('2023/14/'+filename)
    global w,h
    w,h = len(lines[0]), len(lines)
    rocks, cubes, wall = get_rock_locations(lines)
    answer = calculate(rocks, cubes, wall, len(lines), 1000000000)
    return answer


def run():
    a = get_answer()#'test_input.txt')
    print(a)

def time():
    import timeit
    s = timeit.default_timer()
    for _ in range(10):
        get_answer()
    e = timeit.default_timer() - s
    print(e)
    print(e/10)

def profile():
    import cProfile
    cProfile.run('time()')

run()
#time()
#profile()