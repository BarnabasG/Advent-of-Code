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
        
def combine_disks(disk_f, disk_s):
    new_disk = disk_f.copy()
    for index, s in disk_s[::-1]:
        new_disk.insert(index, (-1, s))
    return new_disk

def print_disk(disk):
    for d in disk:
        if d[0] == -1:
            print('.'*d[1], end='')
        else:
            print(str(d[0])*d[1], end='')
    print()

def p2(filename):
    line = list(map(int, next(read_gen(filename))))

    files = line[::2]
    spaces = line[1::2] + [0]

    # disk_f = []
    # disk_s = []
    disk = []
    for i, (f, s) in enumerate(zip(files, spaces)):
        # print(f, s)
        disk.extend([(i, f), (-1, s)])
        # disk_f.append((i, f))
        # disk_s.append((i+1, s))
    
    # print(disk)
    # print(disk_f, disk_s)

    # print_disk(combine_disks(disk_f, disk_s))
    # print_disk(disk)
    # print()


    for i in range(len(disk)-1, -1, -1): #disk_f[::-1]:
        f, s = disk[i]
        if f == -1:
            continue
        for j, (val, size) in enumerate(disk[:i]):
            if val == -1 and size >= s:
                disk[j] = (val, size-s)
                # disk.pop(i)
                disk[i] = (-1, s)
                disk.insert(j, (f, s))
                break
            
        # print_disk(disk)
    
    # print_disk(disk)

    disk = [f for f, s in disk for _ in range(s)]
    # print(disk)
    # print(''.join(str(d) if d != -1 else '.' for d in disk))

    # tot = 0
    # for i, val in enumerate(disk):
    #     print(i, val)
    #     if val == -1:
    #         print()
    #         continue
    #     n = i * val
    #     print(n)
    #     tot += n
    #     print(tot)
    #     print()

    return sum(i * val for i, val in enumerate(disk) if val != -1)

    # for j in range(len(disk_f)-1, -1, -1):
    #     n, size = disk_f[j]
    #     for k, (index, space) in enumerate(disk_s):
    #         print(index, space)
    #         if size <= space:
    #             print('large enough')
    #             print(disk_s[k], (index+1, space-size))
    #             disk_s[index] = (index+1, space-size)
    #             for s in disk_s[index:]:
    #                 s = (s[0]+1, s[1])
    #             print(disk_s)
    #             print(disk_f, disk_f[j], index, (n, size))
    #             disk_f.pop(j)
    #             disk_f.insert(index, (n, size))
    #             print(disk_f)
    #             break
    #     print(disk_f, disk_s)
    #     print_disk(combine_disks(disk_f, disk_s))
    #     print()
        

    # print(disk_f)
    # print(disk_s)

    # reconstruct
    # for index, s in disk_s[::-1]:
    #     disk_f.insert(index, (-1, s))
    
    # print(disk_f)

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
print(p2('2024/9/input.txt'))