def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]



def p1(filename):
    lines = [list(map(int, line.split())) for line in open(filename)]
    count = 0
    for report in lines:
        is_valid = all(
            1 <= abs(b - a) <= 3 and (i < 2 or (b - a) * (a - c) >= 0)
            for i, (a, b, c) in enumerate(zip(report, report[1:], [float('inf')] + report[:-1]))
        )
        count += is_valid
        print(f"{is_valid:<7} {report}")
    print(count)
    return sum(all(1 <= abs(b - a) <= 3 and (i < 2 or (b - a) * (a - c) >= 0) for i, (a, b, c) in enumerate(zip(report, report[1:], [float('inf')] + report[:-1]))) for report in [list(map(int, line.split())) for line in open(filename)])

def p2(filename):
    return sum(any(all(1 <= abs(b - a) <= 3 and (i < 2 or (b - a) * (a - c) >= 0) for i, (a, b, c) in enumerate(zip(x, x[1:], [float('inf')] + x[:-1]))) for x in (report[:j] + report[j+1:] for j in range(len(report)))) for report in [list(map(int, line.split())) for line in open(filename)])


print(p1('2024/2/input.txt'))
print(p2('2024/2/input.txt'))