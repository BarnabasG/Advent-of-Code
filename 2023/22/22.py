from copy import deepcopy

def parse_input(filename):
    def parse(line,i):
        return {
            'p': list(map(list, zip(*(map(int, group.split(',')) for group in line.split('~'))))),
            'i': i,
        }
    with open(filename, 'r') as f:
        return [parse(line.rstrip('\n'),i) for i,line in enumerate(f.readlines())]

def get_collisions(blocks, block, index):
    collisions = []
    for otherblock in blocks:
        if index == otherblock['i']:
            continue
        if all(max(min1, min2) <= min(max1, max2) for (min1, max1), (min2, max2) in zip(block, otherblock['p'])):
            collisions.append(otherblock['i'])
            if len(collisions) > 1:
                break
    return collisions

def drop_blocks(blocks):
    supports = {x['i']:[] for x in blocks}
    max_z = 0
    for i,block in enumerate(blocks):
        while True:
            if block['p'][2][0] == 1 or block['p'][2][1] == 1:
                max_z = max(max_z, block['p'][2][0], block['p'][2][1])
                break
            nxt = deepcopy(block['p'])
            nxt[2][0] -= 1
            nxt[2][1] -= 1
            if min(nxt[2]) <= max_z:
                collisions = get_collisions(blocks[:i], nxt, block['i'])
                if len(collisions) > 0:
                    for c in collisions:
                        supports[block['i']].append(c)
                    max_z = max(max_z, block['p'][2][0], block['p'][2][1])
                    break
            blocks[i]['p'] = nxt
    return supports

def get_answer(filename='input.txt'):
    lines = parse_input('2023/22/'+filename)
    lines = sorted(lines, key=lambda x: min(x['p'][2][0], x['p'][2][1]))
    supports = drop_blocks(lines)
    required = set([x[0] for x in supports.values() if len(x) == 1])
    destroy = len(supports) - len(required)
    return destroy


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
#time(1)
#profile()