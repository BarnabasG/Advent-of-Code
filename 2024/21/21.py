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
    # move_map = {
    #     (-1,0): '^', (1,0): 'v', (0,-1): '<', (0,1): '>'
    # }

    def move_to_str(dy, dx):
        return ('v'*dy if dy > 0 else '^'*(-dy)) + ('>'*dx if dx > 0 else '<'*(-dx))    

    def seq_keypad(char, pos=char_map_keypad['A']):
        target = char_map_keypad[char]
        dy, dx = target[0]-pos[0], target[1]-pos[1]
        # print(dy, dx)
        m = move_to_str(dy, dx)
        move = ''.join(sorted(m)) + 'A' if target[1] == 0 and pos[0] == 2 else m + 'A'
        return move
    
    def seq_remote(char, pos=char_map_remote['A']):
        target = char_map_remote[char]
        dy, dx = target[0]-pos[0], target[1]-pos[1]
        # print(dy, dx)
        m = move_to_str(dy, dx)
        move = ''.join(sorted(m)) + 'A' if pos==char_map_remote['<'] else m + 'A'
        return move, target
    
    def robot_recursion(moves, robot):
        if robot == 0:
            return moves
        
        new_moves = ''
        pointer = char_map_remote['A']
        for move in moves:
            move, pointer = seq_remote(move, pointer)
            new_moves += move
        
        # print(robot_pointers)
        
        return robot_recursion(new_moves, robot - 1)


    
    def multi_step(code, robots=2):
        seq = ''
        # base_pointer = char_map_keypad['A']
        # robot_pointers = [char_map_remote['A'] for _ in range(robots)]
        for char in code:
            command = seq_keypad(char, char_map_keypad['A'])
            command = robot_recursion(command, robots)
            seq += command

        return len(seq)
    
    def extract_num(code):
        return int(''.join([c for c in code if c.isdigit()]))

    for c in codes:
        print(extract_num(c), multi_step(c))

    return sum([extract_num(c)*multi_step(c) for c in codes])


def p2(filename):
    return

## Now undercounting - sort pointer
print(p1('2024/21/input.txt'))
print(p2('2024/21/test_input.txt'))