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
        f, l = None, None
        for i, char in enumerate(line):
            if char.isnumeric():
                f = char
                break
            elif 1==2:#char.isalpha():
                for j in range(min(i, 5), 0):
                    if line[j:] in word_lookup:
                        f = word_lookup[trail[j:]]
                        trail = trail[:j]
                        break
        for i, char in enumerate(line[::-1]):
            if char.isnumeric():
                l = char
                break
            elif 1==2:#char.isalpha():
                for j in range(min(i, 5), 0):
                    if line[j:] in word_lookup:
                        f = word_lookup[trail[j:]]
                        trail = trail[:j]
                        break
        total = int(f"{f}{l}")
        values.append(total)
    
    return values, sum(values)

lines = parse_input()
values, answer = get_answer(lines)
print(values)
print(answer)