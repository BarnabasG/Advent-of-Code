from functools import cache


def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def p1(filename):
    codes = read_lines(filename)

    char_map_keypad = {
        '7': (0,0), '8': (0,1), '9': (0,2), '4': (1,0), '5': (1,1), '6': (1,2), '1': (2,0), '2': (2,1), '3': (2,2), '0': (3,1), 'A': (3,2)
    }
    char_map_remote = {
        '^': (0,1), '<': (1,0), 'v': (1,1), '>': (1,2), 'A': (0,2)
    }

    def move_to_str(dy, dx):
        return ('v'*dy if dy > 0 else '^'*(-dy)) + ('>'*dx if dx > 0 else '<'*(-dx))    

    def seq_keypad(char, pos=char_map_keypad['A']):
        target = char_map_keypad[char]
        dy, dx = target[0]-pos[0], target[1]-pos[1]
        # print('pos, target, dy, dx', pos, target, dy, dx)
        m = move_to_str(dy, dx)
        move = m + 'A' #''.join(sorted(m)) + 'A' if target[1] == 0 and pos[0] == 2 else m + 'A'
        return move, target
    
    def seq_remote(char, pos=char_map_remote['A']):
        target = char_map_remote[char]
        dy, dx = target[0]-pos[0], target[1]-pos[1]
        # print('pos, target, dy, dx', pos, target, dy, dx)
        m = move_to_str(dy, dx)
        move = m + 'A' #''.join(sorted(m)) + 'A' if pos==char_map_remote['<'] else m + 'A'
        return move, target
    
    def robot_recursion(moves, robot):
        if robot == 0:
            return moves
        
        new_moves = ''
        pointer = char_map_remote['A']
        for move in moves:
            # print('robot, move, pointer', robot, move, pointer)
            move, pointer = seq_remote(move, pointer)
            new_moves += move
            # print('new_moves', new_moves)
        # print('robot, move, pointer', robot, move, pointer)

        return robot_recursion(new_moves, robot - 1)


    
    def multi_step(code, robots=2):
        seq = ''
        base_pointer = char_map_keypad['A']
        for char in code:
            # print(char)
            c, base_pointer = seq_keypad(char, base_pointer)
            # print(c)
            command = robot_recursion(c, robots)
            seq += command

        return len(seq)
    
    def extract_num(code):
        return int(code[:-1])

    a = 0
    for c in codes: # only code 879A
        x, y = extract_num(c), multi_step(c)
        print(c, y)
        a += x * y
    
    return a

    # return sum([extract_num(c)*multi_step(c) for c in codes])


def p2(filename):
    return

#### ISSUE - need to make sure the robots can press the nearest keys first
print(p1('2024/21/input.txt'))  # should be 188384
# print(p2('2024/21/test_input.txt'))