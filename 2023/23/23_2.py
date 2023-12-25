import networkx as nx

def parse_input(filename):
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]

def get_nodes(grid):
    nodes = []
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char in '<>v^.':
                nodes.append((i,j))
    return nodes

def traverse(grid, start, target):

    graph = nx.Graph()
    graph.add_node(start)
    graph.add_node(target)

    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v in ".>v":
                for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    ar, ac = r + dr, c + dc
                    if not (0 <= ar < len(grid) and 0 <= ac < len(row)):
                        continue
                    if grid[ar][ac] in ".>v":
                        graph.add_edge((r,c), (ar,ac), weight=1)
    return graph

def longest_path(G, source, target):
    all_paths = list(nx.all_simple_paths(G, source, target))
    max_len = 0
    for path in all_paths:
        length = sum(G.edges[path[i], path[i + 1]]['weight'] for i in range(len(path) - 1))
        if length > max_len:
            max_len = length
    return max_len

def simplify_graph(G):
    H = G.copy()
    simplified = True
    while simplified:
        simplified = False
        for node in list(H.nodes()):
            if H.degree(node) == 2:
                neighbors = list(H.neighbors(node))
                weight = sum(H.get_edge_data(node, n)['weight'] for n in neighbors)
                H.add_edge(*neighbors, weight=weight)
                H.remove_node(node)
                simplified = True
    return H

def visualise(graph):
    import matplotlib.pyplot as plt
    pos = nx.spring_layout(graph)  # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(graph, pos, node_size=700)
    # edges
    nx.draw_networkx_edges(graph, pos)
    # labels
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.axis('off')
    plt.show()


def get_answer(filename='input.txt'):
    grid = parse_input('2023/23/'+filename)
    start = next((0,j) for j, c in enumerate(grid[0]) if c == '.')
    end = next((len(grid)-1,j) for j, c in enumerate(grid[-1]) if c == '.')
    graph = traverse(grid, start, end)
    print(graph)
    graph = simplify_graph(graph)
    print(graph)
    # visualise(graph)

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
#time(1)
#profile()