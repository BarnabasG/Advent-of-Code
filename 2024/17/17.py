from collections import deque
import re


def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def combo(registers, operand):
    combo_map = {
        0: 0, 1: 1, 2: 2, 3: 3,
        4: registers['A'], 
        5: registers['B'], 
        6: registers['C']
    }
    return combo_map.get(operand, 0)

def calculate(registers, opcode, operand, pointer):
    match opcode:
        case 0:
            registers['A'] //= (2**combo(registers, operand))
            return pointer+2, None
        case 1:
            registers['B'] ^= operand
            return pointer+2, None
        case 2:
            registers['B'] = combo(registers, operand) % 8
            return pointer+2, None
        case 3:
            if registers['A'] == 0:
                return pointer+2, None
            else:
                return operand, None
        case 4:
            registers['B'] ^= registers['C']
            return pointer+2, None
        case 5:
            return pointer+2, combo(registers, operand) % 8
        case 6:
            registers['B'] = registers['A'] // (2**combo(registers, operand))
            return pointer+2, None
        case 7:
            registers['C'] = registers['A'] // (2**combo(registers, operand))
            return pointer+2, None


def p1(filename):
    registers = {}
    for line in read_gen(filename):
        if line.startswith('Register'):
            r, v = re.match(r'Register (\w+): (\d+)', line).groups()
            registers[r] = int(v)
        elif line.startswith('Program'):
            program = list(map(int, line.split(' ')[1].split(',')))
            # program = list(zip(p[::2], p[1::2]))
    
    print(registers)
    print(program)

    pointer = 0
    output = []
    while pointer < len(program):
        opcode, operand = program[pointer], program[pointer + 1]
        p, o = calculate(registers, opcode, operand, pointer)
        pointer = p
        if o is not None:
            output.append(o)

    
    return ','.join(map(str, output))
        

def p2(filename):
    registers = {}
    for line in read_gen(filename):
        if line.startswith('Register'):
            r, v = re.match(r'Register (\w+): (\d+)', line).groups()
            registers[r] = int(v)
        elif line.startswith('Program'):
            program = list(map(int, line.split(' ')[1].split(',')))
            # program = list(zip(p[::2], p[1::2]))
    
    print(registers)
    print(program)

    # state_cache = set()

    count = 0
    while True:
        registers['A'] = count
        registers['B'] = 0
        registers['C'] = 0
        pointer = 0
        # output = []
        required = deque(program)
        # invalid  = False

        # state = (tuple(registers), pointer)
        # if state in state_cache:
        #     count += 1
        #     continue
        # state_cache.add(state)

        while pointer < len(program):
            opcode, operand = program[pointer], program[pointer + 1]
            pointer, o = calculate(registers, opcode, operand, pointer)
            if o is not None:
                if not o == required.popleft():
                    break
                if not required:
                    return count
            # state = (tuple(registers), pointer)
            # if state in state_cache:
            #     break
            # state_cache.add(state)
        count += 1




print(p1('2024/17/input.txt'))
print(p2('2024/17/input.txt'))