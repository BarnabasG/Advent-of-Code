from functools import cache


def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def dfs(towel: str, stock: set[str], index: int) -> bool:
    if index == len(towel):
        return True
    
    for s in stock:
        if towel[index:].startswith(s):
            if dfs(towel, stock, index + len(s)):
                return True
    
    return False

def find_path_count(towel, stock):

    @cache
    def dfs_count(index: int) -> bool:
        if index == len(towel):
            return True
        
        count = 0
        for s in stock:
            if towel[index:].startswith(s):
                count += dfs_count(index + len(s))
        
        return count

    return dfs_count(0)

def p1(filename):
    lines = read_lines(filename)
    stock = set(lines[0].split(', '))
    required = lines[2:]
    
    return sum(1 for towel in required if dfs(towel, stock, 0))
  

def p2(filename):
    lines = read_lines(filename)
    stock = set(lines[0].split(', '))
    required = lines[2:]

    return sum(find_path_count(towel, stock) for towel in required)


print(p1('2024/19/input.txt'))
print(p2('2024/19/input.txt'))

from pybencher import Suite

suite = Suite()
filename = '2024/19/input.txt'
suite.add(p1, filename)
suite.add(p2, filename)
suite.run()