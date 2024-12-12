def read_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')

def read_lines(filename):
    with open(filename) as f:
        return [line.rstrip('\n') for line in f.readlines()]

def p1(filename):
    line = list(map(int, next(read_gen(filename))))
    disk = []
    file = True
    count = 0
    for char in line:
        if file:
            disk += [count]*char
            count += 1
        else:
            disk += [-1]*char
        file = not file
    print(disk)
    
    for char in disk[::-1]:
        if char == -1:
            disk.pop()
        else:
            try:
                index = disk.index(-1)
                disk[index] = disk.pop()
            except ValueError:
                break
    print(disk)
    
    return sum(i * val for i, val in enumerate(disk))
        
        

def p2(filename):
    line = list(map(int, next(read_gen(filename))))

    # files = line[::2]
    # spaces = line[1::2]

    # print(spaces)
    # print(files)
    
    # # Create file objects with index and length
    # file_objects = list(enumerate(files))

    # print(file_objects)
    
    # # Track final file placements
    # final_placement = []
    
    # # Process files from right to left
    # for file_index in range(len(file_objects) - 1, -1, -1):
    #     current_index = file_index
    #     file_length = file_objects[current_index][1]
        
    #     # Find the first suitable space from left to right
    #     best_space_index = -1
    #     for i, space_length in enumerate(spaces):
    #         if space_length >= file_length:
    #             best_space_index = i
    #             break
        
    #     # If a suitable space is found, place the file and update space
    #     if best_space_index != -1:
    #         final_placement.append(file_objects[current_index])
    #         spaces[best_space_index] -= file_length
    
    # # Sort final placement based on original file indices
    # # final_placement.sort(key=lambda x: x[0])
    
    # return final_placement

    # files = []
    # gaps = []
    # file = True
    # count = 0
    # for char in line:
    #     if file:
    #         files.append((count, char, True))
    #         count += 1
    #     else:
    #         files.append((0, char, False))
    #         gaps.append(char, len(files)-1)
    #     file = not file
    # # print(disk)
    
    # for count, size, isfile in files[::-1]:
    #     if not isfile:
    #         continue
    #     for gap, index in gaps:
    #         if size <= gap:
    #             files[index] = (count, size, True)
    #             break

    
    # return sum(i * val for i, val in enumerate(disk))


# print(p1('2024/9/input.txt'))
print(p2('2024/9/test_input.txt'))