def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def recursive_expand(lines, i, j, defined, region):
    if (i, j) in defined:
        return region
    
    defined.add((i, j))
    region.add((i, j))
    
    for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        x, y = i + direction[0], j + direction[1]
        if 0 <= x < len(lines) and 0 <= y < len(lines[x]) and lines[x][y] == lines[i][j]:
            recursive_expand(lines, x, y, defined, region)
    
    return region


def p1(filename):
    lines = read_lines(filename)
    regions = []
    defined = set()
    for i, line in enumerate(lines):
        for j in range(len(line)):
            if (i,j) in defined:
                continue
            regions.append(recursive_expand(lines, i, j, defined, set()))
    
    return sum([(len(region) * sum(sum(1 for offset in ((0, 1), (1, 0), (-1, 0), (0, -1)) if (cell[0] + offset[0], cell[1] + offset[1]) not in region) for cell in region)) for region in regions])


def calculate_price_p2(region):
    perimeter = sum(
        sum(1 for offset in ((0, 1), (1, 0), (-1, 0), (0, -1))
            if (cell[0] + offset[0], cell[1] + offset[1]) not in region)
        for cell in region
    )

    p = 0
    for cell in region:
        for offset in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            if (cell[0] + offset[0], cell[1] + offset[1]) not in region:
                p += 1

    print(region, perimeter)
    return 0

def p2(filename):
    lines = read_lines(filename)
    regions = []
    defined = set()
    for i, line in enumerate(lines):
        for j in range(len(line)):
            if (i,j) in defined:
                continue
            regions.append(recursive_expand(lines, i, j, defined, set()))
    
    return sum([calculate_price_p2(region) for region in regions])


print(p1('2024/12/input.txt'))
print(p2('2024/12/test_input.txt'))

# from pybencher import Suite

# filename = '2024/12/input.txt'
# suite = Suite()
# suite.add(p1, filename)
# suite.run()
