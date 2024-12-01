def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def p1(filename):
    lines = read_lines(filename)
    x, y = [], []
    for line in lines:
        a, b = line.split('  ')
        x.append(a)
        y.append(b)

    x = list(map(int, x))
    y = list(map(int, y))
    
    x.sort()
    y.sort()

    tot = 0
    for i in range(len(x)):
        tot += abs(x[i] - y[i])
    
    return tot

def p2(filename):
    lines = read_lines(filename)
    x, y = [], []
    for line in lines:
        a, b = line.split('  ')
        x.append(a)
        y.append(b)

    x = list(map(int, x))
    y = list(map(int, y))

    # print(x, y)

    tot = 0
    for i in x:
        tot += (i * (y.count(i)))
    
    return tot


print(p1('2024/1/input.txt'))
print(p2('2024/1/input.txt'))