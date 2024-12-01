def p1(filename):
    return sum(abs(a - b) for a, b in zip(sorted([int(line.rstrip('\n').split('  ')[0]) for line in open(filename).readlines()]), sorted([int(line.rstrip('\n').split('  ')[1]) for line in [line.rstrip('\n') for line in open(filename).readlines()]])))

def p2(filename):
    return sum(int(x) * sum(1 for line in open(filename).readlines() if line.split()[1] == x) for x in [line.split()[0] for line in open(filename).readlines()])


print(p1('2024/1/input.txt'))
print(p2('2024/1/input.txt'))