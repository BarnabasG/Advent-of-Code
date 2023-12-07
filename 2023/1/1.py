def parse_input(filename='input.txt'):
    with open('2023/1/'+filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
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
    
    return sum(values)

lines = parse_input()#'test_input.txt')
answer = get_answer(lines)
print(answer)