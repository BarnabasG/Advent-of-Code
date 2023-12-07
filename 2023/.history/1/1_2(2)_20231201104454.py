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
    #maps = {}

    for line in lines:
        #f, l = None, None
        
        #found = {k: None for k in word_lookup.keys()}
        max_found = (-1,None)
        min_found = (len(line)+1,None) 
        for word, number in word_lookup.items():
            x = get_indexes(line, word)
            x += get_indexes(line, number)
            if x:
                if max(x) > max_found[0]:
                    max_found = (max(x), number)
                if min(x) < min_found[0]:
                    min_found = (min(x), number)
        
        print(line)
        print(min_found)
        print(max_found)
            
            
            #line = line.replace(word, number)
        
        #f = re.search(r'\d', line).group()
        #l = re.search(r'\d', line[::-1]).group()

        total = int(f"{min_found[1]}{max_found[1]}")
        values.append(total)
        #maps[line] = [min_found, max_found]
    
    return values, sum(values)#, maps

#x = 'abcdefghijcaw'
#print(x[2:4])
#print(x[::-1][2:4])
#print(x[::-1][2:4][::-1])
#print(x[-4:-2])
#print(x[0:2])
#print(get_indexes(x,'z'))


lines = parse_input()#'test_input.txt')
values, answer = get_answer(lines)
print(values)
#print(maps)
print(answer)
