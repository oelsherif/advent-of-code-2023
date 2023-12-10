with open("inputs/10.txt", "r") as File:
    grid = ['.' + line[:-1] + '.' for line in File]

m = len(grid[0])
grid = ['.' * m] + grid + ['.' * m]
n = len(grid)

pipes = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    'L': ['N', 'E'],
    'J': ['N', 'W'],
    '7': ['S', 'W'],
    'F': ['S', 'E'],
    '.': []
}

reverse = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
}

directions = {
    'N': [0, -1],
    'S': [0, 1],
    'E': [1, 0],
    'W': [-1, 0]
}

#find starting position
for y0, row in enumerate(grid):
    for x0, char in enumerate(row):
        if char == 'S':
            break
    if char == 'S':
        break

#find starting direction
for dir in directions.keys():
    dx = directions[dir][0]
    dy = directions[dir][1]
    x, y = x0 + dx, y0 + dy
    char = grid[y][x]
    if reverse[dir] in pipes[char]:
        starting_dir = dir
        break

x, y, dir = x0, y0, starting_dir
steps = 0
while True:
    steps += 1
    dx = directions[dir][0]
    dy = directions[dir][1]
    new_x, new_y = x + dx, y + dy
    if (char := grid[new_y][new_x]) == 'S':
        break
    pipe = pipes[char]
    rev_dir = reverse[dir]
    if rev_dir == pipe[0]:
        dir = pipe[1]
    else:
        dir = pipe[0]
    x, y = new_x, new_y
print(steps//2)
   