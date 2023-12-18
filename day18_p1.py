with open("inputs/18.txt", "r") as File:
    commands = []
    for line in File:
        dir, num, color = line.split()
        line = (dir, int(num), color[2:-1])
        commands.append(line)

colors = {}
dirs = ['R', 'L', 'U', 'D']
def new_pos(x: int, y: int, dir: str) -> (int, int):
    if dir == 'R':
        return x+1, y
    if dir == 'L':
        return x-1, y
    if dir == 'U':
        return x, y-1
    if dir == 'D':
        return x, y+1
    
def in_grid(x: int, y: int) -> bool:
    if x < 0 or x >= n_cols or y < 0 or y >= n_rows:
        return False
    return True

x0, y0 = 0, 0
x, y = x0, y0
for command in commands:
    dir, num, color = command
    for _ in range(num):
        x, y = new_pos(x, y, dir)
        colors[x, y] = color

x_min = min(pos[0] for pos in colors)
y_min = min(pos[1] for pos in colors)

x_shift = -x_min + 1
y_shift = -y_min + 1

new_colors = {(color[0] + x_shift, color[1] + y_shift): colors[color] for color in colors}

n_cols = max(pos[0] for pos in new_colors) + 2
n_rows = max(pos[1] for pos in new_colors) + 2

grid = [['.'] * n_cols for _ in range(n_rows)]
for x, y in new_colors:
    grid[y][x] = '#'

x0, y0 = 0, 0
out_symbol = ' '
grid[y0][x0] = out_symbol
currents = [(x0, y0)]
while True:
    new_currents = []
    for x, y in currents:
        for dir in dirs:
            new_x, new_y = new_pos(x, y, dir)
            if not in_grid(new_x, new_y):
                continue
            if grid[new_y][new_x] != '.':
                continue
            grid[new_y][new_x] = out_symbol
            new_currents.append((new_x, new_y))
    if not new_currents:
        break
    currents = new_currents.copy()

# for row in grid:
#     print(''.join(row))

ans_p1 = sum([n_cols - row.count(out_symbol) for row in grid])
print(f"Part 1 answer: {ans_p1}")