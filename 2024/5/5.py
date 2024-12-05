def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def p1(filename):
    lines = read_lines(filename)
    orders = [l.split('|') for l in lines[:lines.index('')]]
    pagegroups = [l.split(',') for l in lines[lines.index('')+1:]]

    result = {}
    for a, b in orders:
        if a not in result:
            result[a] = {'comes_after': set(), 'comes_before': set()}
        if b not in result:
            result[b] = {'comes_after': set(), 'comes_before': set()}
        result[a]['comes_before'].add(b)
        result[b]['comes_after'].add(a)

    tot = 0
    for pages in pagegroups:
        valid = True
        for i, p in enumerate(pages):
            if any(prev in result[p]['comes_before'] for prev in pages[:i]) or any(after in result[p]['comes_after'] for after in pages[i+1:]):
                valid = False
                break
            if not valid:
                break
        if valid:
            tot += int(pages[len(pages)//2])

    return tot



def find_largest(pages, result):
    largest, index = pages[0], 0
    for i, p in enumerate(pages[1:]):
        if largest in result[p]['comes_before']:
            largest = p
            index = i+1
    return largest, index

def find_order(pages, result):
    order = []
    while pages:
        largest, index = find_largest(pages, result)
        order.append(largest)
        pages.pop(index)
    return order
    

def p2(filename):
    lines = read_lines(filename)
    orders = [l.split('|') for l in lines[:lines.index('')]]
    pagegroups = [l.split(',') for l in lines[lines.index('')+1:]]

    result = {}
    for a, b in orders:
        if a not in result:
            result[a] = {'comes_after': set(), 'comes_before': set()}
        if b not in result:
            result[b] = {'comes_after': set(), 'comes_before': set()}
        result[a]['comes_before'].add(b)
        result[b]['comes_after'].add(a)

    tot = 0
    for pages in pagegroups:
        valid = True
        for i, p in enumerate(pages):
            if any(prev in result[p]['comes_before'] for prev in pages[:i]) or any(after in result[p]['comes_after'] for after in pages[i+1:]):
                valid = False
                break
            if not valid:
                break
        if not valid:
            new_order = find_order(pages, result)
            tot += int(new_order[len(new_order)//2])

    return tot



print(p1('2024/5/input.txt'))
print(p2('2024/5/input.txt'))