import re

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
    for l in lines:
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", l)
        # print(matches)
        for m in matches:
            tot += int(m[0]) * int(m[1])
    return tot

# def p2(filename):
#     lines = read_lines(filename)
#     tot = 0
#     for l in lines:
#         print(l)
#         # l = re.sub(r"don't\(\).+?do\(\)|don't\(\).*$", '', l)
#         commands = re.split(r"(don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\))", l)
#         print(commands)
#         active = True
#         for c in commands:
#             print(c)
#             if c == "don't()":
#                 print("don't")
#                 active = False
#             elif c == "do()":
#                 print("do")
#                 active = True
#             elif c.startswith("mul"):
#                 print("mul", active)
#                 if active:
#                     matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", c)
#                     for m in matches:
#                         print(int(m[0]) * int(m[1]))
#                         tot += int(m[0]) * int(m[1])
#                         print(tot)
#     return tot


def p2(filename):
    lines = read_lines(filename)
    tot = 0

    for l in lines:
        l = re.sub(r"don't\(\).*?do\(\)|don't\(\).*?$", '', l)
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", l)
        tot += sum(int(a) * int(b) for a, b in matches)
    return tot


print(p1('2024/3/input.txt'))
print(p2('2024/3/input.txt'))