import re
from functools import reduce

def map_values(seed_range, mappings):
    mapped_values = set()
    unmapped_values = set([seed_range])

    for (s_start, s_end), shift in mappings.items():
        _unmapped_values = set()
        for (r_start, r_end) in unmapped_values:
            if r_end <= s_start or r_start >= s_end:
                _unmapped_values.add((r_start, r_end))
                continue

            if r_end > s_end:
                _unmapped_values.add((s_end, r_end))
            
            if r_start < s_start:
                _unmapped_values.add((r_start, s_start))
            
            overlap_min, overlap_max = max(r_start, s_start), min(r_end, s_end)
            if overlap_min < overlap_max:
                mapped_values.add((overlap_min + shift, overlap_max + shift))
        
        unmapped_values = _unmapped_values
    
    return list(mapped_values | unmapped_values)

def get_answer(filename='2023/5/input.txt'):
    with open(filename, 'r') as f:
        maps = {}
        _seeds = [int(x) for x in re.findall(r'\d+', f.readline().split(':')[1])]
        seed_ranges = [(_seeds[i],_seeds[i]+_seeds[i+1]) for i in range(0, len(_seeds), 2)]
        f.readline()

        for l in f:
            l = l.rstrip('\n')
            if 'map' in l:
                continue
            if l.strip() == '':
                seed_ranges = list(reduce(lambda x,y: x+y, [map_values(r, maps) for r in seed_ranges], []))
                maps = {}
                continue
            destination,source,range_length = [int(x) for x in re.findall(r'\d+', l)]
            maps[(source, source+range_length)] = destination - source
        
        seed_ranges = list(reduce(lambda x,y: x+y, [map_values(r, maps) for r in seed_ranges], []))
        return min(seed_ranges, key=lambda x: x[0])[0]


answer = get_answer()
print(answer)