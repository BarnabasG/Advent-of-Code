from collections import deque
import networkx as nx

def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

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

def traverse(track):
    graph = nx.Graph()
    # graph.add_edge('S', start, weight=0)
    # graph.add_edge('E', end, weight=0)

    for coord in track:
        x, y = coord
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in track:
                graph.add_edge(coord, (new_x, new_y), weight=1)
    
    return graph

# def simplify_graph(G):
#     H = G.copy()
#     simplified = True
#     while simplified:
#         simplified = False
#         for node in list(H.nodes()):
#             if H.degree(node) == 2:
#                 neighbors = list(H.neighbors(node))
#                 weight = sum(H.get_edge_data(node, n)['weight'] for n in neighbors)
#                 H.add_edge(*neighbors, weight=weight)
#                 H.remove_node(node)
#                 simplified = True
#     return H

def get_cost(graph, start, end):
    shortest_path = nx.shortest_path(graph, start, end)
    cost = sum(graph[u][v]['weight'] for u, v in zip(shortest_path[:-1], shortest_path[1:]))
    return cost

def find_cheats(graph, track, start, end):
    cheats = set()
    paths = {}
    base_cost = get_cost(graph, start, end)
    for coord in track:
        for move in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
            x, y = coord
            dx, dy = move
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in track and ((new_x, new_y), (x, y)) not in cheats:
                graph.add_edge(coord, (new_x, new_y), weight=2)
                cost_saving = base_cost - get_cost(graph, start, end)
                # print(f'cheat: {coord} -> {(new_x, new_y)}: {cost}')
                # if cost < base_cost:
                if cost_saving >= 100:
                    print(f'cheat: {coord} -> {(new_x, new_y)}: {cost_saving}')
                    paths[((x, y), (new_x, new_y))] = cost_saving
                graph.remove_edge(coord, (new_x, new_y))
                cheats.add(((x, y), (new_x, new_y)))

    return sorted(paths.items(), key=lambda x: x[1], reverse=True)

def find_paths(graph, start, end):
    paths_with_costs = {}
    
    all_paths = nx.all_simple_paths(graph, source=start, target=end)
    
    for path in all_paths:
        cost = sum(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
        paths_with_costs[tuple(path)] = cost
    
    return paths_with_costs


### Very slow
def p1_graph(filename):
    lines = read_lines(filename)
    walls = set()
    track = set()
    start, end = None, None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                case '#':
                    walls.add((x, y))
                case 'S':
                    track.add((x, y))
                    start = (x, y)
                case 'E':
                    track.add((x, y))
                    end = (x, y)
                case '.':
                    track.add((x, y))
    print(walls)
    print(track)
    print(start)
    print(end)

    graph = traverse(track)
    cheat_paths = find_cheats(graph, track, start, end)
    return len(cheat_paths)
    # graph_simple = simplify_graph(graph_cheats)
    # # visualise(graph_simple)
    # find_paths(graph_simple, start, end)


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def calculate_cheats(grid, offsets):
    grid, reachable_coords = flood_fill_maze(grid)
    # print(reachable_coords)
    # [print(g) for g in grid]
    return sum(count_cheats(grid, r, c, offsets) for r, c in reachable_coords)

def offsets_within_distance(n):
    return [(r, c, abs(r) + abs(c)) for r in range(-n, n + 1) for c in range(-n, n + 1) if 0 < abs(r) + abs(c) <= n]

def count_cheats(maze, r, c, offsets):
    val, cheats = maze[r][c], 0
    threshold = val - 100

    for dr, dc, dist in offsets:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != "#":
            if threshold - dist >= maze[nr][nc]:
                cheats += 1

    return cheats

def flood_fill_maze(grid):
    end_pos = find_character(grid, "E")
    queue, reachable_coords = deque([(0, end_pos)]), []
    visited = set()

    while queue:
        dist, (r, c) = queue.popleft()
        if (r, c) in visited:
            continue

        grid[r][c] = dist
        visited.add((r, c))
        reachable_coords.append((r, c))

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] in {".", "S"}:
                queue.append((dist + 1, (nr, nc)))

    return grid, reachable_coords

def find_character(grid, char):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == char:
                return r, c

def p2(filename):
    lines = read_lines(filename)
    return calculate_cheats([list(l) for l in lines], offsets_within_distance(20))

def p1(filename):
    lines = read_lines(filename)
    return calculate_cheats([list(l) for l in lines], offsets_within_distance(2))




import networkx

data = read_lines('2024/20/input.txt')

m, n = len(data), len(data[0])
ex = ey = -1

G = networkx.Graph()

for i in range(m):
    for j in range(n):
        if data[i][j] in '.SE':
            G.add_node((i, j))

for i in range(m):
    for j in range(n):
        if data[i][j] in '.SE':
            if data[i][j] == 'E':
                ex, ey = i, j
            for dx, dy in [(0, 1), (1, 0)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and data[nx][ny] != '#':
                    G.add_edge((i, j), (nx, ny))

shortest_paths = dict(networkx.shortest_path_length(G, target=(ex, ey)))

def get_reachable(x, y, max_dist):
    reachable = []
    for dx in range(-max_dist, max_dist + 1):
        remaining_dist = max_dist - abs(dx)
        for dy in range(-remaining_dist, remaining_dist + 1):
            if dx == dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and data[nx][ny] in '.SE':
                reachable.append((nx, ny))
    return reachable


def solve(cheat_size):
    res = 0
    for node in G.nodes:
        i, j = node
        reachable = get_reachable(i, j, cheat_size)
        for dx, dy in reachable:
            cost = abs(i - dx) + abs(j - dy)
            savings = shortest_paths[(i, j)] - (shortest_paths[(dx, dy)] + cost)
            if savings >= 100:
                res += 1
    return res

def p1_graph_new(filename):
    return solve(2)

def p2_graph_new(filename):
    return solve(20)



print(p1('2024/20/input.txt'))
print(p2('2024/20/input.txt'))

print(p1_graph_new('2024/20/input.txt'))
print(p2_graph_new('2024/20/input.txt'))

from pybencher import Suite

suite = Suite()
filename = '2024/20/input.txt'

suite.add(p1, filename)
suite.add(p2, filename)
suite.add(p1_graph_new, filename)
suite.add(p2_graph_new, filename)

suite.run()