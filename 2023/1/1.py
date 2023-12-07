def parse_input(filename='input.txt'):
    with open('1/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    print(lines)
    return lines

def get_answer(lines):
    values = []
    for line in lines:
        f, l = None, None
        for char in line:
            if char.isnumeric():
                f = char
                break
        for char in line[::-1]:
            if char.isnumeric():
                l = char
                break
        total = int(f"{f}{l}")
        values.append(total)
    
    return values, sum(values)

lines = parse_input('test_input.txt')
values, answer = get_answer(lines)
print(values)
print(answer)