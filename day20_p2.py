from math import lcm
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
    state = flipflop_state[module]
    if pulse == 'high':
        return None
    dests = destinations[module]
    if state == 'off':
        flipflop_state[module] = 'on'
        for dest in dests:
            queue.append((module, dest, 'high'))
        return None
    else:
        flipflop_state[module] = 'off'
        for dest in dests:
            queue.append((module, dest, 'low'))
        return None

def activate_conjunction(source, module, pulse):
    dests = destinations[module]
    conjunction_memories[module][source] = pulse
    memories = conjunction_memories[module]
    # if module == 'dn' and any(memory == 'high' for memory in memories.values()):
    #     print(i, memories)
    if module == 'dn':
        for j, memory in enumerate(memories.values()):
            if memory == 'high' and dn_tracker[j] == 0:
                dn_tracker[j] = i
    if all(memory == 'high' for memory in memories.values()):
        for dest in dests:
            queue.append((module, dest, 'low'))
        return None
    else:
        for dest in dests:
            queue.append((module, dest, 'high'))
        return None

def press_button():
    global is_done
    while queue:
        source, module, pulse = queue.popleft()
        if not module in modules:
            continue
        if module_type[module] == '%':
            activate_flipflop(source, module, pulse)
        else:
            activate_conjunction(source, module, pulse)

##SIMILAR TO DAY 8, A SKETCHY LCM METHOD
##Module dn has to get 4 highs to send a low to rx
##We find out when each of its 4 pulses gets a high, then LCM
dn_tracker = [0]*len(conjunction_memories['dn'])
queue0 = deque()
queue = deque()
for dest in destinations['broadcaster']:
    queue0.append(('broadcaster', dest, 'low'))
n_presses = 10000
is_done = False
i = 1
for i in range(1, n_presses):
    queue = deepcopy(queue0)
    press_button()
    if all(num for num in dn_tracker):
        break
ans_p2 = lcm(*dn_tracker)
print(f"Part 2 answer: {ans_p2}")