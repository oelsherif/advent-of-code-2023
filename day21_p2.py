from collections import defaultdict
from copy import deepcopy

with open("inputs/21.txt", "r") as File:
    grid = [list(line[:-1]) for line in File]

#Really unhappy with my solution for today. A figured out the "main tricks" but did a lot of math off the page
#ugly math and ugly code that I wouldn't be able to explain easily and probably won't understand in a few days.

def in_grid(x, y, n_cols, n_rows) -> bool:
    if x < 0 or x >= n_cols or y < 0 or y >= n_rows:
        return False
    return True

dirs = ['N', 'E', 'S', 'W']

def new_pos(x, y, dir):
    if dir == 'E':
        return x+1, y
    if dir == 'W':
        return x-1, y
    if dir == 'N':
        return x, y-1
    if dir == 'S':
        return x, y+1

#Find Start
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == 'S':
            x0, y0 = x, y
            grid[y0][x0] = '.'

##Ok so a lot of input analysis and math are going to happen
#Observations
# 1- Start is in exact center of grid. The way N,S,E,W of Start is clear in all directions 
# 2- The number of steps will take us exactly to the edge of a grid in each direction
# 3- Steps are odd. Grid length is in 4k-1. We will reach edge directly N,S,E,W in center grid, won't in adjacent grids and so on.
            
            
grid_size = len(grid)
grid_half_size = grid_size // 2
n_steps = 26501365
#print(n_steps%131) #Same as half_size
real_expansion = n_steps//131 #number of grids added in each cardinal direction

def expand_grid(grid0, expansion):
    grid = deepcopy(grid0)
    for _ in range(2*expansion):
        grid += grid0
    grid = [row * (2*expansion + 1) for row in grid]
    return grid

def end_plots(grid, n_steps):
    n_rows = len(grid)
    n_cols = len(grid[0])
    x0, y0 = n_cols//2, n_rows//2
    currents = [(x0, y0)]
    count_even, count_odd = 0, 0
    #even count is even number of steps away
    for step in range(n_steps):
        new_currents = []
        for x, y in currents:
            for dir in dirs:
                new_x, new_y = new_pos(x, y, dir)
                if not in_grid(new_x, new_y, n_cols, n_rows):
                    continue
                if grid[new_y][new_x] != '.':
                    continue
                new_currents.append((new_x, new_y))
                grid[new_y][new_x] = 'O'
                if step % 2:
                    count_even += 1
                else:
                    count_odd += 1
        if not new_currents:
            break
        currents = new_currents.copy()
    return count_even, count_odd

def n_full(i):
    if i == 0:
        return 1
    else:
        return 4 * i

totals = []
fulls = []
vertex_grids = 25956 #got the totals steps in the 4 vertices by running it on one expansion and subtracting the inner grad
trials = 11
# for expansion in range(0, trials, 2):
#     new_grid = expand_grid(grid, expansion)
#     n_steps = expansion*grid_size+grid_half_size
#     even, odd = end_plots(new_grid, n_steps)
#     full = 0
#     total = odd
#     for i in range(expansion):
#         if i%2:
#             full += n_full(i) * 7410
#         else:
#             full += n_full(i) * 7363

#     totals.append(total)
#     fulls.append(full)
#     print(expansion, total, full, total - full - vertex_grids)
# ##Got the difference. It's equal to (expansion-1)*29589

extras = 29589
def get_answer(expansion):
    full = 0
    for i in range(expansion):
        if i%2:
            full += n_full(i) * 7410
        else:
            full += n_full(i) * 7363
    return full + vertex_grids + extras*(expansion-1)

ans_p2 = get_answer(real_expansion)
print(f"Part 2 answer: {ans_p2}")