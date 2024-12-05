def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def p1(filename):
    return

def p2(filename):
    return


print(p1('2024/9/test_input.txt'))
print(p2('2024/9/test_input.txt'))