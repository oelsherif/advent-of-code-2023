from collections import defaultdict
with open("inputs/22.txt", "r") as File:
    lines = [line[:-1] for line in File]

blocks = {}
for i, line in enumerate(lines):
    start, end = line.split('~')
    x1, y1, z1 = [int(num) for num in start.split(',')]
    x2, y2, z2 = [int(num) for num in end.split(',')]
    blocks[i+1] = [(x1, x2), (y1, y2), (z1, z2)]

x_max = max([block[0][1] for block in blocks.values()]) + 1
y_max = max([block[1][1] for block in blocks.values()]) + 1
z_max = max([block[2][1] for block in blocks.values()]) + 1

grid3d = [[[0]*x_max for _ in range(y_max)] for _ in range(z_max)]

for x in range(0, x_max):
    for y in range(0, y_max):
        grid3d[0][y][x] = -1

for i, block in blocks.items():
    xs, ys, zs = block
    x1, x2 = xs
    y1, y2 = ys
    z1, z2 = zs
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                grid3d[z][y][x] = i

##Let the blocks fall
is_change = True
while (is_change):
    is_change = False
    for i, block in blocks.items():
        xs, ys, zs = block
        x1, x2 = xs
        y1, y2 = ys
        z1, z2 = zs
        all_empty = True
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if grid3d[z1-1][y][x]:
                    all_empty = False
                    break
            if all_empty == False:
                break
        if all_empty == False:
            continue
        is_change = True
        blocks[i][2] = (z1-1, z2-1)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid3d[z2][y][x] = 0
                grid3d[z1-1][y][x] = i

essential_blocks = set()
supported_by = defaultdict(set)
dependants = defaultdict(set)
total_dependants = defaultdict(set) #values would fall without key

for i, block in blocks.items():
    xs, ys, zs = block
    x1, x2 = xs
    y1, y2 = ys
    z1, z2 = zs
    supports = set()
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (support := grid3d[z1-1][y][x]) > 0:
                supported_by[i].add(support)
                dependants[support].add(i)
    if len(supported_by[i]) == 1:
        (sole_supporter,) = supported_by[i]
        total_dependants[sole_supporter].add(i)

ans_p1 = len(blocks) - len(total_dependants)
print(f"Part 1 answer: {ans_p1}")

sorted_blocks = sorted(blocks, key=lambda block: blocks[block][2][1], reverse=True) #sort blocks from top to bottom
for main_block in sorted_blocks:
    total_deps = total_dependants[main_block].copy()
    for total_dep in total_deps:
        total_dependants[main_block] |= total_dependants[total_dep]
    deps = dependants[main_block].copy()
    for dep in deps:
        dependants[main_block] |= dependants[dep]
    is_change = True
    while is_change:
        is_change = False
        pot_deps = dependants[main_block] - total_dependants[main_block]
        for pot_dep in pot_deps:
            remaining_supporters = supported_by[pot_dep] - total_dependants[main_block]
            if remaining_supporters:
                continue
            is_change = True
            total_dependants[main_block].add(pot_dep)
    
ans_p2 = sum((len(fallen) for fallen in total_dependants.values()))
print(f"Part 2 answer: {ans_p2}")
