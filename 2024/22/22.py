from collections import defaultdict
from functools import cache, reduce
from itertools import pairwise


def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

# @cache
# def mix(n, m):
#     return n ^ m

# @cache
# def prune(n):
#     return n % 16777216

@cache
def next_number(n):
    n ^= n << 6 & 0xFFFFFF
    n ^= n >> 5 & 0xFFFFFF
    return n ^ n << 11 & 0xFFFFFF
    # a = prune(mix(n*64, n))
    # b = prune(mix(a//32, a))
    # return prune(mix(b*2048, b))

def apply_itrs(n, itrs):
    return reduce(lambda x, _: next_number(x), range(itrs), n)

def p1(filename):
    return sum(apply_itrs(n, 2000) for n in list(map(int, read_lines(filename))))

def p2(filename):
    lines = map(int, read_lines(filename))
    bananas = defaultdict(int)
    for s in lines:
        number_chain = [s] + [s := next_number(s) for _ in range(2000)]
        cost_chain = [b % 10 for b in number_chain]
        diff_chain = [b - a for a,b in pairwise(cost_chain)]

        seen_patterns = set()
        for i in range(len(diff_chain) - 4):
            pattern = tuple(diff_chain[i:i+4])
            if pattern not in seen_patterns:
                bananas[pattern] += cost_chain[i+4]
                seen_patterns.add(pattern)

    return max(bananas.values())


print(p1('2024/22/input.txt'))
print(p2('2024/22/input.txt'))

from pybencher import Suite

suite = Suite()
filename = '2024/22/input.txt'

suite.add(p1, filename)
suite.add(p2, filename)

# suite.run()