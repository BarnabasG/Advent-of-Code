from functools import reduce

flip = lambda a: 2 if a==1 else 3

def parse_input(filename):
    rules = {}
    with open(filename, 'r') as f:
        for l in f.readlines():
            if l == '\n' or l[0] == '{':
                continue
            else:
                parts = l.rstrip('\n')[:-1].split('{')[1].split(',')
                rules[l.split('{')[0]] = [(p[0],0 if '<' in p else 1, int(p.split(':')[0][2:]), p.split(':')[1]) for p in parts[:-1]]
                rules[l.split('{')[0]].append(parts[-1])
    return rules

def apply_filter(conditions, xmas):
    for condition in conditions:
        if not xmas[condition[0]][0] <= condition[2] <= xmas[condition[0]][1]:
            continue
        if condition[1] == 0:
            xmas[condition[0]][1] = condition[2] - 1
        elif condition[1] == 1:
            xmas[condition[0]][0] = condition[2] + 1
        elif condition[1] == 2:
            xmas[condition[0]][1] = condition[2]
        elif condition[1] == 3:
            xmas[condition[0]][0] = condition[2]
    return xmas

def paths(rules, flow):
    p, next_flows = [], []
    for r,rul in rules.items():
        if rul[-1] == flow:
            p.append([r]+[(c[0],flip(c[1]),c[2]) for c in rul[:-1]])
            next_flows.append(r)
        for i, cond in enumerate(rul[:-1]):
            if cond[3] == flow:
                p.append([r,(cond[0],cond[1],cond[2])]+[(c[0],flip(c[1]),c[2]) for c in rul[:i]])
                next_flows.append(r)
    return p, next_flows

def iterate(routes, flowmap):
    _routes = []
    for route in routes:
        for flow in flowmap[route[0]]:
            _routes.append([flow[0],apply_filter(flow[1:], route[1])])
    return _routes

def get_answer(filename='input.txt'):
    rules = parse_input('2023/19/'+filename)
    flowmap = {}
    flowmap['A'], nxt = paths(rules, 'A')
    nxt = set(nxt)
    while nxt:
        _nxt = set()
        for flow in nxt:
            flowmap[flow], n = paths(rules, flow)
            _nxt.update(n)
        nxt = _nxt - nxt
    
    routes = []
    for route in flowmap['A']:
        xmas = {
            'x': [1,4000],
            'm': [1,4000],
            'a': [1,4000],
            's': [1,4000]
        }
        routes.append([route[0],apply_filter(route[1:], xmas)])
    
    found = []
    while routes:
        found.extend([r[1] for r in routes if r[0] == 'in'])
        routes = [r for r in routes if r[0] != 'in']
        routes = iterate(routes, flowmap)
    
    #print(found)
    
    return sum((reduce(lambda x,y: x*y, [r[1]-r[0]+1 for r in f.values()]) for f in found))


def run():
    a = get_answer()#'test_input.txt')
    print(a)

def time():
    import timeit
    s = timeit.default_timer()
    for _ in range(50):
        get_answer()
    e = timeit.default_timer() - s
    print(e)
    print(e/50)

def profile():
    import cProfile
    cProfile.run('time()')

#run()
time()
#profile()