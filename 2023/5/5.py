import re

def parse_input(filename='input.txt'):
    with open('2023/5/'+filename, 'r') as f:
        return [x.rstrip('\n') for x in f.readlines() if x != '\n']

def get_values(lines):
    maps = {}
    maps['seeds'] = [int(x) for x in re.findall(r'\d+', lines.pop(0).split(':')[1])]
    current_map = None
    for l in lines:
        if 'map' in l:
            current_map = l.split(' ')[0]
            maps[current_map] = []
            continue
        maps[current_map].append([int(x) for x in re.findall(r'\d+', l)])
    return maps
    
def get_saved_values(maps):
    saved_values = {k:[] for k in maps if k != 'seeds'}
    for m in maps:
        if m == 'seeds':
            continue
        for thisrange in maps[m]:
            saved_values[m].append((thisrange[1],thisrange[1]+thisrange[2]-1,thisrange[0]-thisrange[1]))
    
    return saved_values


def get_answer(maps):
    seeds = maps['seeds']
    seed_locations = {}
    value_ranges = get_saved_values(maps)

    for seed in seeds:
        search_value = seed
        for m in maps:
            if m == 'seeds':
                continue
            for ranges in value_ranges[m]:
                if ranges[0] <= search_value <= ranges[1]:
                    search_value += ranges[2]
                    break
        seed_locations[seed] = search_value

    return min(seed_locations.values())

lines = parse_input()
maps = get_values(lines)
answer = get_answer(maps)
print(answer)