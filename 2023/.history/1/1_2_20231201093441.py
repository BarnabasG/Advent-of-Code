def parse_input(filename='input.txt'):
    with open('1/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    print(lines)
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
            elif char.isalpha():
                for j in range(0, min(i+1, 6)):
                    x = line[j:i+1]
                    if line[j:i] in word_lookup:
                        f = word_lookup[line[j:i]]
                        break
        for i, char in enumerate(line[::-1]):
            if char.isnumeric():
                l = char
                break
            elif char.isalpha():
                for j in range(0, min(i+1, 6)):
                    x = line[::-1][i:j]
                    if line[i+1:j] in word_lookup:
                        f = word_lookup[line[j:i]]
                        break
        total = int(f"{f}{l}")
        values.append(total)
    
    return values, sum(values)

lines = parse_input('test_input.txt')
values, answer = get_answer(lines)
print(values)
print(answer)