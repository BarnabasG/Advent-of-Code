import networkx as nx

def parse_input(filename):
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]

def get_nodes(grid):
    nodes = []
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char in '<>v^':
                nodes.append((i,j))
    return nodes

def traverse(grid, start, target):

    graph = nx.DiGraph()
    graph.add_node(start)
    graph.add_node(target)
    nodes = get_nodes(grid)
    [graph.add_node(n) for n in nodes]
    ends = [{
        'c': start,
        'p': None,
        'pn': start,
        's': 0
    }]
    while ends:
        new_ends = []
        for end in ends:
            for n in ((0,1),(0,-1),(1,0),(-1,0)):
                point = (end['c'][0]+n[0],end['c'][1]+n[1])
                if 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0]):
                    if point == target:
                        graph.add_edge(end['pn'], point, weight=end['s']+1)
                    elif grid[point[0]][point[1]] != '#' and point != end['p'] and point not in [x['c'] for x in new_ends]:
                        match grid[point[0]][point[1]]:
                            case '.':
                                new_ends.append({'c':point, 'p':end['c'], 'pn':end['pn'], 's':end['s']+1})
                            case '>':
                                if point[1] != end['p'][1] - 1:
                                    graph.add_edge(end['pn'], point, weight=end['s']+1)
                                    new_ends.append({'c':point, 'p':end['c'], 'pn':point, 's':0})
                            case '<':
                                if point[1] != end['p'][1] + 1:
                                    graph.add_edge(end['pn'], point, weight=end['s']+1)
                                    new_ends.append({'c':point, 'p':end['c'], 'pn':point, 's':0})
                            case '^':
                                if point[0] != end['p'][0] + 1:
                                    graph.add_edge(end['pn'], point, weight=end['s']+1)
                                    new_ends.append({'c':point, 'p':end['c'], 'pn':point, 's':0})
                            case 'v':
                                if point[0] != end['p'][0] - 1:
                                    graph.add_edge(end['pn'], point, weight=end['s']+1)
                                    new_ends.append({'c':point, 'p':end['c'], 'pn':point, 's':0})
        ends = new_ends
    return graph

def longest_path(G, source, target):
    all_paths = list(nx.all_simple_paths(G, source, target))
    max_len = 0
    for path in all_paths:
        length = sum(G.edges[path[i], path[i + 1]]['weight'] for i in range(len(path) - 1))
        if length > max_len:
            max_len = length
    
    return max_len

def get_answer(filename='input.txt'):
    grid = parse_input('2023/23/'+filename)
    start = next((0,j) for j, c in enumerate(grid[0]) if c == '.')
    end = next((len(grid)-1,j) for j, c in enumerate(grid[-1]) if c == '.')
    graph = traverse(grid, start, end)
    longest = longest_path(graph, start, end)
    return longest

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
#time(10)
#profile()