from itertools import combinations
from sympy import var, Eq, solve

def parse_input(filename):
    def parse(l):
        return [list(map(int, p.split(','))) for p in l.split('@')]
    with open(filename, 'r') as f:
        return [parse(line.rstrip('\n')) for line in f.readlines()]

def solver(lines):
    sx = var("sx")
    sy = var("sy")
    sz = var("sz")

    vx = var("vx")
    vy = var("vy")
    vz = var("vz")

    eq = []
    for l in lines:
        ps, vs = l

        ts = "t{}".format(len(eq) // 3)
        exec(f'{ts} = var("{ts}")')

        eq.append(Eq(eval(f"sx + vx * {ts}"), eval(f"ps[0] + vs[0] * {ts}")))
        eq.append(Eq(eval(f"sy + vy * {ts}"), eval(f"ps[1] + vs[1] * {ts}")))
        eq.append(Eq(eval(f"sz + vz * {ts}"), eval(f"ps[2] + vs[2] * {ts}")))

        # 3 pos, 3 vs + 3 ts minimum length, otherwise same solution with more calcaution
        if len(eq) > 9:
            break

    s = solve(eq)[0]
    return s[sx] + s[sy] + s[sz]


def get_answer(filename='input.txt'):
    return solver(parse_input('2023/24/'+filename))

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

run()
#time(50)
#profile()