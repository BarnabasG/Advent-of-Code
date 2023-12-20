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
    pulses = {0: 0, 1: 0}

    def press_button():
        stack = [('button', Signal.LOW, 'broadcaster')]
        while stack:
            pulses[1] += (count_high := sum(s[1].value for s in stack))
            pulses[0] += len(stack) - count_high
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
                if sum(maps[node]['rec'].values()) == len(maps[node]['rec']):
                    stack.extend([(node,Signal.LOW,m) for m in maps[node]['out']])
                else:
                    stack.extend([(node,Signal.HIGH,m) for m in maps[node]['out']])
        return stack
    
    for _ in range(1000):
        press_button()

    return pulses[0] * pulses[1]


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

#run()
time()
#profile()