def parse_input(filename='./input.txt'):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]

def get_answer(lines):
    values = []
    for line in lines:
        f, l = None, None
        for char in line:
            if char.isnumeric():
                f = char
        for char in line[::-1]:
            if char.isnumeric():
                l = char
        total = int(f"{f}{l}")
        values.append(total)
    
    return values, sum(values)

lines = parse_input()
values, answer = get_answer(lines)
print(values)
print(answer)