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
                    if line[j:i+1] in word_lookup:
                        f = word_lookup[line[j:i+1]]
                        break
            if f is not None:
                break
        for i, char in enumerate(line[::-1]):
            if char.isnumeric():
                l = char
                break
            elif char.isalpha():
                for j in range(0, min(i+1, 6)):
                    #x = line[::-1][j:i][::-1]
                    x = line[-i:-j]
                    if line[-i:-j] in word_lookup:
                        f = word_lookup[line[-i:-j]]
                        break
            if l is not None:
                break
        total = int(f"{f}{l}")
        values.append(total)
    
    return values, sum(values)

#x = 'abcdefghij'
#print(x[2:4])
#print(x[::-1][2:4])
#print(x[::-1][2:4][::-1])
#print(x[-4:-2])


lines = parse_input('test_input.txt')
values, answer = get_answer(lines)
print(values)
print(answer)