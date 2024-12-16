def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def find_consecutive_boxes(walls, boxes, player, direction):
    next_pos = (player[0] + direction[0], player[1] + direction[1])
    
    if next_pos in walls:
        return None
    
    if next_pos not in boxes:
        return []
    
    remaining_boxes = boxes - {next_pos}
    further_boxes = find_consecutive_boxes(walls, remaining_boxes, next_pos, direction)
    
    if further_boxes is None:
        return None
    
    return [next_pos] + further_boxes


def print_grid(walls, boxes, player, MAX_X, MAX_Y):
    for i in range(MAX_Y):
        for j in range(MAX_X):
            if (i, j) in walls:
                print('#', end='')
            elif (i, j) in boxes:
                print('O', end='')
            elif (i, j) == player:
                print('@', end='')
            else:
                print('.', end='')
        print()


def p1(filename):
    lines = read_lines(filename)
    # MAX_X = len(lines[0])
    # MAX_Y = None
    walls = set()
    boxes = set()
    instructions = []
    for i, line in enumerate(lines):
        if len(line) > 0 and line[0] in ('^', 'v', '<', '>'):
            instructions += line
            # if MAX_Y is None:
            #     MAX_Y = i
            continue
        for j, char in enumerate(line):
            if char == '#':
                walls.add((i, j))
            elif char == 'O':
                boxes.add((i, j))
            elif char == '@':
                player = (i, j)

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }


    for instruction in instructions:
        # print_grid(walls, boxes, player, MAX_X, MAX_Y)
        direction = directions[instruction]
        boxes_infront = find_consecutive_boxes(walls, boxes, player, direction)
        # print('instruction', instruction, 'boxes_infront', boxes_infront)
        if boxes_infront is None:
            continue
        for box in boxes_infront[::-1]:
            new_box_pos = (box[0] + direction[0], box[1] + direction[1])
            boxes.remove(box)
            boxes.add(new_box_pos)
        player = (player[0] + direction[0], player[1] + direction[1])

                
    # print_grid(walls, boxes, player, MAX_X, MAX_Y)

    return sum((100*b[0] + b[1] for b in boxes))
            


def find_boxes_to_push(walls, boxes, player, direction):
    next_positions = {player}
    all_boxes = set()

    while next_positions:
        n = set()
        for pos in next_positions:
            next_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if next_pos in walls:
                return None
            
            box = next((t for t in boxes if next_pos in t), None)

            if box is not None:
                all_boxes.add(tuple(box))
                if direction[1] == 0:
                    n.add(box[0])
                    n.add(box[1])
                else:
                    n.add(box[0] if box[0] != pos else box[1])
        
        next_positions = n
    
    return all_boxes

def p2(filename):
    lines = read_lines(filename)
    # MAX_X = len(lines[0])*2
    # MAX_Y = None
    walls = set()
    boxes = []
    instructions = []
    
    for i, line in enumerate(lines):
        if len(line) > 0 and line[0] in ('^', 'v', '<', '>'):
            instructions += line
            # if MAX_Y is None:
            #     MAX_Y = i - 1
            #     continue
        
        for j, char in enumerate(line):
            pos1, pos2 = (i, 2*j), (i, 2*j+1)
            if char == '#':
                walls.add(pos1)
                walls.add(pos2)
            elif char == 'O':
                boxes.append(sorted([pos1, pos2]))
            elif char == '@':
                player = pos1
    
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    
    for instruction in instructions:
        direction = directions[instruction]
        boxes_infront = find_boxes_to_push(walls, boxes, player, direction)

        if boxes_infront is None:
            continue

        for box in boxes_infront:
            boxes[boxes.index(sorted(box))] = [
                (t[0] + direction[0], t[1] + direction[1])
                for t in box
            ]

        player = (player[0] + direction[0], player[1] + direction[1])
        
    return sum((100*b[0] + b[1] for b in [b[0] for b in boxes]))


print(p1('2024/15/input.txt'))
print(p2('2024/15/input.txt'))