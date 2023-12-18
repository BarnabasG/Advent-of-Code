int_mapping = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}

def parse_input(filename):
    parse = lambda line: (int_mapping[int(line[-2])], (int(line[-7:-2], base=16)))
    with open(filename, 'r') as f:
        return [parse(line.rstrip('\n')) for line in f.readlines()]

def dig(instructions):
    c = (0,0)
    visited = [c]
    for instruct in instructions:
        c = (c[0]+instruct[0][0]*instruct[1], c[1]+instruct[0][1]*instruct[1])
        visited.append(c)
    return visited

def shoelace_area(coords, edges):
    # shoelace/gauss formula
    area = 0
    for i in range(len(coords)-1):
        y1, x1 = coords[i]
        y2, x2 = coords[i + 1]
        area += x1 * y2 - x2 * y1
    area = abs(area) // 2 + edges // 2 + 1
    return area

def get_answer(filename='input.txt'):
    lines = parse_input('2023/18/'+filename)
    v = dig(lines)
    edges = sum([x[1] for x in lines])
    a = shoelace_area(v, edges)
    return a

def run():
    a = get_answer()#'test_input.txt')
    print(a)

def time():
    import timeit
    s = timeit.default_timer()
    for _ in range(500):
        get_answer()
    e = timeit.default_timer() - s
    print(e)
    print(e/500)

def profile():
    import cProfile
    cProfile.run('time()')

run()
#time()
#profile()