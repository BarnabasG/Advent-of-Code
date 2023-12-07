import re

def parse_input(filename='input.txt'):
    with open('1/'+filename, 'r') as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    print(lines)
    return lines

word_lookup = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_indexes(line, search):
    l1 = []
    length = len(line)
    index = 0
    while index < length:
        i = line.find(search, index)
        if i == -1:
            return l1
        l1.append(i)
        index = i + 1
    return l1

def get_answer(lines):
    values = []
    maps = {}

    for line in lines:
        #f, l = None, None
        
        found = {k: [] for k in word_lookup.keys()}
        for word, number in word_lookup.items():
            if word in line:
                found[word].append(line.index(word))
            #if 
            
            
            line = line.replace(word, number)
        
        f = re.search(r'\d', line).group()
        l = re.search(r'\d', line[::-1]).group()

        total = int(f"{f}{l}")
        values.append(total)
        maps[line] = [f, l]
    
    return values, sum(values), maps

x = 'abcdefghijcaw'
#print(x[2:4])
#print(x[::-1][2:4])
#print(x[::-1][2:4][::-1])
#print(x[-4:-2])
#print(x[0:2])
print(get_indexes(x,'c'))


#lines = parse_input('test_input.txt')
#values, answer, maps = get_answer(lines)
#print(values)
#print(maps)
#print(answer)
