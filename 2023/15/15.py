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

def hash_char(c):
    return (ord(c) * 17) % 256


def get_answer(filename='input.txt'):
    lines = parse_input('2023/15/'+filename)
    print(lines)
    answer = sum(hash_str(s) for s in lines if s != ',')

    #chars = open(filename, 'r').readline().rstrip('\n')
    #nswer = sum(hash_char(c) for c in chars if c != ',')
    

    return answer

answer = get_answer()#'test_input.txt')
print(answer)