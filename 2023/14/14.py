def parse_input(filename):
    with open(filename, 'r') as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]

def get_rock_locations(lines):
    rocks, cubes = [], []
    for i, row in enumerate(lines):
        for j, item in enumerate(row):
            if item == 'O':
                rocks.append((i,j))
            elif item == '#':
                cubes.append((i,j))
    wall = [(-1, i) for i in range(len(lines[0]))]
    return rocks, cubes, wall

def calculate_load(rocks,max_load):
    return sum([(max_load-rock[0]) for rock in rocks])

def tilt_north(rocks, cubes, wall):
    #moves = []
    #_rocks = rocks[:]
    
    #print(wall)
    #print(sorted(rocks, key=lambda x: x[0]))
    for i,rock in enumerate(sorted(rocks, key=lambda x: x[0])):
        first_cube = max([c for c in cubes+rocks+wall if c[1] == rock[1] and c[0] < rock[0]], key=lambda x: x[0])
        #print(rock, first_cube)
        if first_cube: rocks[i] = (first_cube[0]+1, first_cube[1]) 
        #moves.append((first_cube[0]+1, first_cube[1]) if first_cube else None)
        # moves.append((rock, (first_cube[0]+1, first_cube[1]) if first_cube else None))
    
    #print(moves)
    return rocks



def draw_map(lines, rocks, cubes):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (i,j) in rocks:
                print('O', end='')
            elif (i,j) in cubes:
                print('#', end='')
            else:
                print('.', end='')
        print()


def get_answer(filename='input.txt'):
    lines = parse_input('2023/14/'+filename)
    rocks, cubes, wall = get_rock_locations(lines)
    #print(rocks, cubes)
    #draw_map(lines, rocks, cubes)
    rocks = tilt_north(rocks, cubes, wall)
    #print(rocks)
    #draw_map(lines, rocks, cubes)
    answer = calculate_load(rocks, len(lines))
    


    return answer

answer = get_answer()#'test_input.txt')
print(answer)