from math import lcm
from enum import Enum
class Signal(Enum):
    HIGH = 1
    LOW = 0

def parse_input(filename):
    maps = {}
    conjunctions = []
    def parse(l):
        parts = l.split(' -> ')
        pulses = parts[1].split(', ')
        if parts[0][0] == 'b':
            node = parts[0]
            maps[node] = {'out': pulses}
        else:
            module = parts[0][0]
            node = parts[0][1:]
            if module == '&':
                conjunctions.append(node)
                maps[node] = {'mod': module, 'out': pulses}
            else:
                maps[node] = {'mod': module, 'out': pulses, 'on': 0}
    
    def build_conjuctions():
        for conj in conjunctions:
            maps[conj]['rec'] = {k:0 for k,v in maps.items() if conj in v['out']}

    with open(filename, 'r') as f:
        [parse(line.rstrip('\n')) for line in f.readlines()]
        build_conjuctions()
        return maps


def get_answer(filename='input.txt'):
    maps = parse_input('2023/20/'+filename)


    def press_button():
        stack = [('button', Signal.LOW, 'broadcaster')]
        while stack:
            #pulses[1] += (count_high := sum(s[1].value for s in stack))
            #pulses[0] += len(stack) - count_high
            stack = handle_signals(stack)

    def handle_signals(signals):
        stack = []
        for sender, strength, node in signals:
            if node == 'broadcaster':
                stack.extend([(node,Signal.LOW,m) for m in maps[node]['out']])
                continue

            if node not in maps:
                continue

            if maps[node]['mod'] == '%':
                if strength == Signal.HIGH:
                    continue
                elif maps[node]['on'] == 0:
                    maps[node]['on'] = 1
                    stack.extend([(node,Signal.HIGH,m) for m in maps[node]['out']])
                else:
                    maps[node]['on'] = 0
                    stack.extend([(node,Signal.LOW,m) for m in maps[node]['out']])

            elif maps[node]['mod'] == '&':
                maps[node]['rec'][sender] = strength.value
                signal = Signal.LOW if sum(maps[node]['rec'].values()) == len(maps[node]['rec']) else Signal.HIGH
                #print(node, maps[node]['rec'], signal)
                if signal == Signal.LOW and node not in cycles:
                    #print(node, cycles, itr)
                    cycles[node] = itr
                stack.extend([(node,signal,m) for m in maps[node]['out']])
        return stack
    
    #print(maps)
    target = 'rx'
    #print([v['out'] for v in maps.values()])
    # rx_pointer = [k for k,v in maps.items() if target in v['out']]
    rx_pointer = next(k for k,v in maps.items() if target in v['out'])
    print(rx_pointer)
    rx_pointer_pointers = maps[rx_pointer]['rec'].keys()
    print(rx_pointer_pointers)
    
    cycles = {}
    itr = 0
    while True:
        itr += 1
        if itr % 10 == 0:
            print(itr)
        press_button()
        #print(cycles)
        if all(item in cycles for item in rx_pointer_pointers):
            break
    
    print(cycles)
    
    answer = lcm(*(cycles[p] for p in rx_pointer_pointers))
    return answer
        
### TODO: Broke the lcm cycle caculation - needs fixing

# Benchmarking
def run():
    a = get_answer()#'test_input.txt')
    print(a)

def time():
    def pretty_time(t):
        import datetime
        units = {
            'ps': 1e-12,
            'ns': 1e-9,
            'μs': 1e-6,
            'ms': 1e-3,
            's': 1,
        }
        for unit, ratio in units.items():
            factor = 59.95 if unit == 's' else 999.5
            if t < factor * ratio:
                num = f'{t/ratio:#.3g}'.rstrip('.')
                return f'{num}{unit}'
        return str(datetime.timedelta(seconds=int(round(t)))).removeprefix('0:')
    
    import timeit
    n = 50
    s = timeit.default_timer()
    for _ in range(n):
        get_answer()
    e = timeit.default_timer() - s
    print('{}: {}/itr'.format(pretty_time(e), pretty_time(e/n)))

def profile():
    import cProfile
    cProfile.run('time()')

run()
#time()
#profile()