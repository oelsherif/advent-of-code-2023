from collections import defaultdict

with open("inputs/21.txt", "r") as File:
    grid = [list(line[:-1]) for line in File]

n_rows = len(grid)
n_cols = len(grid[0])

def in_grid(x, y) -> bool:
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

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == 'S':
            x0, y0 = x, y
            grid[y0][x0] = '.'

n_steps = 64
starting_parity = (x0 + y0) % 2
target_parity = int(starting_parity ^ (n_steps % 2))
visited = defaultdict(list)
currents = [(x0, y0)]
count = 0
for step in range(n_steps):
    new_currents = []
    for x, y in currents:
        for dir in dirs:
            new_x, new_y = new_pos(x, y, dir)
            if not in_grid(new_x, new_y):
                continue
            if grid[new_y][new_x] != '.':
                continue
            new_currents.append((new_x, new_y))
            grid[new_y][new_x] = 'O'
            if (new_x + new_y) % 2 == target_parity:
                count += 1
    if not new_currents:
        break
    currents = new_currents.copy()

ans_p1 = count
print(f"Part 1 answer: {ans_p1}")
