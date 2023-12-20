from collections import defaultdict, deque
from copy import deepcopy

with open("inputs/20.txt", "r") as File:
    lines = [line[:-1].split() for line in File]

module_type = {}
destinations = {}
for line in lines:
    if line[0] == 'broadcaster':
        module = 'broadcaster'
        type = '*'
    else:
        module = line[0][1:]
        type = line[0][0]
    module_type[module] = type
    dests = line[2:]
    for i, dest in enumerate(dests):
        dests[i] = dest.replace(',', '')
    destinations[module] = dests

modules = list(destinations.keys())
flipflops = [module for module in modules if module_type[module] == '%']
conjunctions = [module for module in modules if module_type[module] == '&']
flipflop_state = {flipflop: 'off' for flipflop in flipflops}
conjunction_memories = defaultdict(dict)
for source, dests in destinations.items():
    for dest in dests:
        if dest in conjunctions:
            conjunction_memories[dest][source] = 'low'

def activate_flipflop(source, module, pulse):
    global count_low
    global count_high
    state = flipflop_state[module]
    if pulse == 'high':
        return None
    dests = destinations[module]
    if state == 'off':
        flipflop_state[module] = 'on'
        count_high += len(dests)
        for dest in dests:
            queue.append((module, dest, 'high'))
        return None
    else:
        flipflop_state[module] = 'off'
        count_low += len(dests)
        for dest in dests:
            queue.append((module, dest, 'low'))
        return None

def activate_conjunction(source, module, pulse):
    global count_low
    global count_high
    dests = destinations[module]
    conjunction_memories[module][source] = pulse
    memories = conjunction_memories[module]
    if all(memory == 'high' for memory in memories.values()):
        count_low += len(dests)
        for dest in dests:
            queue.append((module, dest, 'low'))
        return None
    else:
        count_high += len(dests)
        for dest in dests:
            queue.append((module, dest, 'high'))
        return None


def press_button():
    global count_low
    count_low += len(queue) + 1
    while queue:
        source, module, pulse = queue.popleft()
        if not module in modules:
            continue
        if module_type[module] == '%':
            activate_flipflop(source, module, pulse)
        else:
            activate_conjunction(source, module, pulse)

queue0 = deque()
queue = deque()
for dest in destinations['broadcaster']:
    queue0.append(('broadcaster', dest, 'low'))
n_presses = 1000
count_low = 0
count_high = 0
for _ in range(n_presses):
    queue = deepcopy(queue0)
    press_button()

ans_p1 = count_low * count_high
print(f"Part 1 answer: {ans_p1}")

