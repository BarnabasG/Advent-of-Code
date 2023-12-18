def parse_input(filename):
    with open(filename, 'r') as f:
        return f.readline().rstrip('\n').split(',')

def hash_str(string):
    total = 0
    for c in string:
        total += ord(c)
        total *= 17
        total %= 256
    return total

def calculate(boxes):
    total = 0
    for k,v in boxes.items():
        for i, item in enumerate(v.values()):
            total += (k+1) * (i+1) * item
    return total


def get_answer(filename='input.txt'):
    lines = parse_input('2023/15/'+filename)
    print(lines)
    boxes = {i: {} for i in range(256)}
    for s in lines:
        if '=' in s:
            l,b = s.split('=')
            h = hash_str(l)
            boxes[h][l] = int(b)
        else:
            l = s[:-1]
            h = hash_str(l)
            boxes[h].pop(l, None)
    
    answer = calculate(boxes)            
    return answer

answer = get_answer()#'test_input.txt')
print(answer)