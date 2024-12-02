def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def p1(filename):
    lines = read_lines(filename)
    tot = 0
    for line in lines:
        elements = line.split()
        elements = list(map(int, elements))
        e_f, e_b = elements[:], elements[:]
        e_f.sort()
        e_b.sort(reverse=True)
        if not elements == e_f and not elements == e_b:
            continue
        a = elements[0]
        l = True
        for e in elements[1:]:
            if abs(int(a) - int(e)) > 3 or abs(int(a) - int(e)) == 0:
                l = False
                break
            a = e
        if l:
            tot += 1
    return tot


def is_safe(report):
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if not 1 <= diff <= 3:
            return False
        if i > 1 and ((report[i] - report[i - 1] > 0 and report[i - 1] - report[i - 2] < 0) or (report[i] - report[i - 1] < 0 and report[i - 1] - report[i - 2] > 0)):
            return False
    return True

def p2(filename):
    lines = read_lines(filename)
    tot = 0
    for line in lines:
        elements = list(map(int, line.split()))
        if is_safe(elements):
            tot += 1
            continue
        for i in range(len(elements)):
            modified_report = elements[:i] + elements[i+1:]
            if is_safe(modified_report):
                tot += 1
                break
    return tot


print(p1('2024/2/input.txt'))
print(p2('2024/2/input.txt'))