def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def is_safe(report):
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if i > 1 and diff * (report[i - 1] - report[i - 2]) < 0:
            return False
    return True

def is_safe_p2(report):
    fault = False
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            if fault:
                return False
            fault = True
            continue
        if i > 1 and diff * (report[i - 1] - report[i - 2]) < 0:
            if fault:
                return False
            fault = True
    return True

def p1(filename):
    return sum(1 for line in read_lines(filename) if is_safe(list(map(int, line.split()))))

def p2(filename):
    return sum(1 for line in read_lines(filename) if is_safe_p2(list(map(int, line.split()))))

print(p1('2024/2/input.txt'))
print(p2('2024/2/input.txt'))