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

dirs_p2 = ['N', 'E', 'S', 'W']
dirs_p1 = {
    '.': ['N', 'E', 'S', 'W'],
    '^': ['N'],
    '>': ['E'],
    'v': ['S'],
    '<': ['W'],
}
opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

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

x0, y0 = i, 0

for i, char in enumerate(grid[-1]):
    if char == '.':
        break

x_end, y_end = i, n_rows - 1

#### Part 1
t1 = time.time()
currents = [((x0, y0, 'S'),[])] #first tuple is position and direction, second is a list of previous junctions
path_lengths = []
steps = 0
while (True):
    new_currents = []
    for current in currents:
        x, y, dir = current[0]
        juncs = current[1]
        new_juncs = deepcopy(juncs)
        if x == x_end and y == y_end:
            path_lengths.append(steps)
        tile = grid[y][x]
        ultra_new_currents = [] #just for tiles reachable from this tile
        for new_dir in dirs_p1[tile]:
            if new_dir == opposite[dir]:
                continue
            new_x, new_y = new_pos(x, y, new_dir)
            if not in_grid(new_x, new_y):
                continue
            if grid[new_y][new_x] == '#':
                continue
            if (new_x, new_y) in juncs:
                continue
            ultra_new_currents.append((new_x, new_y, new_dir))
        if len(ultra_new_currents) > 1:
            new_juncs.append((x, y))
        for ultra_new_current in ultra_new_currents:
            new_currents.append((ultra_new_current, new_juncs))
    if not new_currents:
        break
    currents = deepcopy(new_currents)
    steps += 1

t2 = time.time()
print(t2 - t1)
ans_p1 = max(path_lengths)
print(f"Part 1 answer: {ans_p1}")

# #### Part 2
# t1 = time.time()
# currents = [((x0, y0, 'S'),[])] #first tuple is position and direction, second is a list of previous junctions
# path_lengths = []
# steps = 0
# while (True):
#     new_currents = []
#     for current in currents:
#         x, y, dir = current[0]
#         juncs = current[1]
#         new_juncs = deepcopy(juncs)
#         if x == x_end and y == y_end:
#             path_lengths.append(steps)
#         tile = grid[y][x]
#         ultra_new_currents = [] #just for tiles reachable from this tile
#         for new_dir in dirs_p2:
#             if new_dir == opposite[dir]:
#                 continue
#             new_x, new_y = new_pos(x, y, new_dir)
#             if not in_grid(new_x, new_y):
#                 continue
#             if grid[new_y][new_x] == '#':
#                 continue
#             if (new_x, new_y) in juncs:
#                 continue
#             ultra_new_currents.append((new_x, new_y, new_dir))
#         if len(ultra_new_currents) > 1:
#             new_juncs.append((x, y))
#         for ultra_new_current in ultra_new_currents:
#             new_currents.append((ultra_new_current, new_juncs))
#     if not new_currents:
#         break
#     currents = deepcopy(new_currents)
#     steps += 1

# t2 = time.time()
# print(t2 - t1)
# ans_p2 = max(path_lengths)
# print(f"Part 2 answer: {ans_p2}")

