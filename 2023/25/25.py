from functools import reduce
import networkx as nx

def parse_input(filename):
    def parse(l):
        a, b = l.split(': ')
        b = b.split(' ')
        return [(a,c) for c in b]
    with open(filename, 'r') as f:
        return list(reduce(lambda x,y: x+y, [parse(line.rstrip('\n')) for line in f.readlines()], []))

def generate_graph(lines):
    G = nx.Graph()
    G.add_edges_from(lines)
    return G

def visualise(graph):
    import matplotlib.pyplot as plt
    pos = nx.spring_layout(graph)  # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(graph, pos, node_size=700)
    # edges
    nx.draw_networkx_edges(graph, pos)
    # labels
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif')
    plt.axis('off')
    plt.show()

def cut_edges(graph):
    cut = nx.minimum_edge_cut(graph)
    return graph.remove_edges_from(cut)

def get_answer(filename='input.txt'):
    lines = parse_input('2023/25/'+filename)
    G = generate_graph(lines)
    print(G)
    cut_edges(G)
    # visualise(G)
    components = list(nx.connected_components(G))
    for i, component in enumerate(components):
        print(f"Group {i+1}: {len(component)} nodes")
    return len(components[0]) * len(components[1])


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