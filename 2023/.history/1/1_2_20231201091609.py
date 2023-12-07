def parse_input(filename='1/input.txt'):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    return lines

word_lookup = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def get_answer(lines):
    values = []
    for line in lines:
        f, l, trail = None, None, trail
        for char in line:
            if char.isnumeric():
                f = char
                break
            elif char.isalpha():
                trail += char
                for i in range(min(len(trail), 5), 0):
                    if trail[i:] in word_lookup:
                        f = word_lookup[trail[i:]]
                        trail = trail[:i]
                        break
        for char in line[::-1]:
            if char.isnumeric():
                l = char
                break
            elif char.isalpha():
                trail += char
                for i in range(min(len(trail), 5), 0):
                    if trail[i:] in word_lookup:
                        f = word_lookup[trail[i:]]
                        trail = trail[:i]
                        break
        total = int(f"{f}{l}")
        values.append(total)
    
    return values, sum(values)

lines = parse_input()
values, answer = get_answer(lines)
print(values)
print(answer)