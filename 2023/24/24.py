from itertools import combinations

def parse_input(filename):
    def parse(l):
        return [list(map(int, p.split(','))) for p in l.split('@')]
    with open(filename, 'r') as f:
        return [parse(line.rstrip('\n')) for line in f.readlines()]

def coeff(x, y, vx, vy):
    a = vy / vx
    b = y - (x * vy) / vx
    return a, b

get_time = lambda d, d0, v: (d - d0) / v
    
def check_intersection(atom1, atom2, min_xy: int, max_xy: int):

    x1, y1, vx1, vy1 = atom1[0][0], atom1[0][1], atom1[1][0], atom1[1][1]
    x2, y2, vx2, vy2 = atom2[0][0], atom2[0][1], atom2[1][0], atom2[1][1]

    c1_a, c1_b = coeff(x1, y1, vx1, vy1)
    c2_a, c2_b = coeff(x2, y2, vx2, vy2)

    if c1_a == c2_a:
        return False
    
    x = (c2_b - c1_b) / (c1_a - c2_a)    
    y = c1_a * x + c1_b
    if x < min_xy or x > max_xy or y < min_xy or y > max_xy:
        return False
    
    tx1 = get_time(x, x1, vx1)
    tx2 = get_time(x, x2, vx2)
    if tx1 < 0 or tx2 < 0:
        return False
    
    return True


def get_answer(filename='input.txt'):
    lines = parse_input('2023/24/'+filename)
    collisions = 0
    comb = combinations(lines, 2)
    for c in comb:
        if check_intersection(c[0], c[1], 200000000000000, 400000000000000):
            collisions += 1
    
    return collisions


# Benchmarking
def run():
    a = get_answer()#'test_input.txt')
    print(a)

def time(n=50):
    def pretty_time(t):
        import datetime
        units = {
            'ps': 1e-12,
            'ns': 1e-9,
            'μs': 1e-6,
            'ms': 1e-3,
            's': 1,
        }
        for unit, ratio in units.items():
            factor = 59.95 if unit == 's' else 999.5
            if t < factor * ratio:
                num = f'{t/ratio:#.3g}'.rstrip('.')
                return f'{num}{unit}'
        return str(datetime.timedelta(seconds=int(round(t)))).removeprefix('0:')
    
    import timeit
    s = timeit.default_timer()
    for _ in range(n):
        get_answer()
    e = timeit.default_timer() - s
    print('{}: {}/itr'.format(pretty_time(e), pretty_time(e/n)))

def profile():
    import cProfile
    cProfile.run('time()')

#run()
time(50)
#profile()