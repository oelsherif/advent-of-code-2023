from copy import deepcopy
import time

with open("inputs/23.txt", "r") as File:
    grid = [list(line[:-1]) for line in File]

n_rows = len(grid)
n_cols = len(grid[0])

def in_grid(x, y) -> bool:
    if x < 0 or x >= n_cols or y < 0 or y >= n_rows:
        return False
    return True

dirs = ['N', 'E', 'S', 'W']
dirs_p1 = {
    '.': ['N', 'E', 'S', 'W'],
    '^': ['N'],
    '>': ['E'],
    'v': ['S'],
    '<': ['W'],
}

def new_pos(x, y, dir):
    if dir == 'E':
        return x+1, y
    if dir == 'W':
        return x-1, y
    if dir == 'N':
        return x, y-1
    if dir == 'S':
        return x, y+1

for i, char in enumerate(grid[0]):
    if char == '.':
        break

x_start, y_start = i, 0

for i, char in enumerate(grid[-1]):
    if char == '.':
        break

x_end, y_end = i, n_rows - 1

def longest_walk(grid, is_part1):
    '''return the length of the longest possible walk. For part1 you cannot go up slopes'''
    ##Find all junctions
    x0, y0 = x_start, y_start
    junctions = [(x0, y0), (x_end, y_end)]
    currents = [(x0, y0)]
    new_currents = deepcopy(currents)
    new_grid = deepcopy(grid)
    new_grid[y0][x0] = 'O'
    while new_currents:
        new_currents = []
        for current in currents:
            x, y = current
            tile = grid[y][x]
            count_hashes = 0
            for new_dir in dirs:
                new_x, new_y = new_pos(x, y, new_dir)
                if not in_grid(new_x, new_y):
                    continue
                new_tile = new_grid[new_y][new_x]
                count_hashes += (new_tile == '#')
                if is_part1 and new_dir not in dirs_p1[tile]:
                    continue
                if new_tile in '#O':
                    continue
                new_currents.append((new_x, new_y))
                new_grid[new_y][new_x] = 'O'
            if count_hashes <= 1:
                junctions.append((x, y))
        currents = deepcopy(new_currents)

    #Find the distance to reach a junction from adjacent junctions
    reachable_junctions = {}
    for junction in junctions:
        steps_to_junc = {}
        steps = 0
        x0, y0 = junction
        if x0 == x_end and y0 == y_end:
            continue
        currents = [(x0, y0)]
        new_currents = deepcopy(currents)
        new_grid = deepcopy(grid)
        new_grid[y0][x0] = 'O'
        while new_currents:
            steps += 1
            new_currents = []
            for current in currents:
                x, y = current
                tile = grid[y][x]
                for new_dir in dirs:
                    new_x, new_y = new_pos(x, y, new_dir)
                    if not in_grid(new_x, new_y):
                        continue
                    new_tile = new_grid[new_y][new_x]
                    if new_tile in '#O':
                        continue
                    if is_part1 and new_dir not in dirs_p1[tile]:
                        continue
                    new_grid[new_y][new_x] = 'O'
                    if ((new_x, new_y)) in junctions:
                        steps_to_junc[(new_x, new_y)] = steps
                        continue
                    new_currents.append((new_x, new_y))
            currents = deepcopy(new_currents)
        reachable_junctions[junction] = deepcopy(steps_to_junc)

    #calculate the length of all paths
    currents = [[0, (x_start, y_start)]]
    new_currents = deepcopy(currents)
    final_list = []
    while new_currents:
        new_currents = []
        for current in currents:
            steps = current[0]
            junc = current[-1]
            if junc == (x_end, y_end):
                final_list.append(current)
                continue
            new_juncs = reachable_junctions[junc]
            for new_junc in new_juncs:
                if new_junc in current:
                    continue
                new_steps = steps + new_juncs[new_junc]
                new_current = [new_steps] + current[1:] + [new_junc]
                new_currents.append(new_current)
        currents = new_currents
    return max(l[0] for l in final_list)

t1 = time.time()
ans_p1 = longest_walk(grid, True)
t2 = time.time()
ans_p2 = longest_walk(grid, False)
t3 = time.time()

print(f"Part 1 answer: {ans_p1}")
#print(t2 - t1)
#print()
print(f"Part 2 answer: {ans_p2}")
#print(t3 - t2)
