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

left = {
    'N': 'W',
    'S': 'E',
    'E': 'N',
    'W': 'S',
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

#Make loop in new grid, with all non-used pipes set to .
new_grid = [ '.' * m for i in range(n) ]
new_grid[y0] = new_grid[y0][:x0] + 'S' + new_grid[y0][x0+1:]
x, y, dir = x0, y0, starting_dir
while True:
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
    new_row = new_grid[y]
    new_grid[y] = new_row[:x] + char + new_row[x+1:]

#Mark immediate left, right sides of loop in new grid, one would be the outside and one the inside, we don't know yet
lefts, rights = set(), set()
x, y, dir = x0, y0, starting_dir
while True:
    dx = directions[dir][0]
    dy = directions[dir][1]
    new_x, new_y = x + dx, y + dy
    left_dir = left[dir]
    left_dx, left_dy = directions[left_dir][0], directions[left_dir][1]
    left_x, left_y = x + left_dx, y + left_dy
    if new_grid[left_y][left_x] == '.':
        new_grid[left_y] = new_grid[left_y][:left_x] + '0' + new_grid[left_y][left_x + 1:]
        lefts.add( (left_x, left_y) )

    right_dir = reverse[left[dir]]
    right_dx, right_dy = directions[right_dir][0], directions[right_dir][1]
    right_x, right_y = x + right_dx, y + right_dy
    if new_grid[right_y][right_x] == '.':
        new_grid[right_y] = new_grid[right_y][:right_x] + '1' + new_grid[right_y][right_x + 1:]
        rights.add( (right_x, right_y) )

    if (char := grid[new_y][new_x]) == 'S':
        break
    pipe = pipes[char]
    rev_dir = reverse[dir]
    if rev_dir == pipe[0]:
        dir = pipe[1]
    else:
        dir = pipe[0]
    x, y = new_x, new_y
    ##Adding stuff here
    left_x, left_y = x + left_dx, y + left_dy
    if new_grid[left_y][left_x] == '.':
        new_grid[left_y] = new_grid[left_y][:left_x] + '0' + new_grid[left_y][left_x + 1:]
        lefts.add( (left_x, left_y) )
    right_x, right_y = x + right_dx, y + right_dy
    if new_grid[right_y][right_x] == '.':
        new_grid[right_y] = new_grid[right_y][:right_x] + '1' + new_grid[right_y][right_x + 1:]
        rights.add( (right_x, right_y) )
    #end of new stuff
    ## NEW STUFF FIXED IT! WAS OFF BY ONE
    ## This causes the marking of cells to the left/right of current cell AND next cell in line
    ## which handles a specific corner case

    new_row = new_grid[y]
    new_grid[y] = new_row[:x] + char + new_row[x+1:]

#Expand lefts and rights in all directions, then print length of the one that doesn't hit grid border
for index, to_check in enumerate([lefts, rights]):
    index = str(index)
    is_inside = True
    all_cells = to_check.copy()
    while True:
        new_cells = set()
        for x, y in to_check:
            if x == 0 or x == m-1 or y == 0 or y == n-1:
                is_inside = False
                break
            for dir in directions.keys():
                dx = directions[dir][0]
                dy = directions[dir][1]
                new_x, new_y = x + dx, y + dy
                char = new_grid[new_y][new_x]
                if char == '.':
                    new_grid[new_y] = new_grid[new_y][:new_x] + index + new_grid[new_y][new_x+1:]
                    new_cells.add( (new_x, new_y) )
        if not is_inside:
            break
        to_check = new_cells - all_cells
        all_cells = all_cells.union(new_cells)
        if not to_check:
            break
    if is_inside:
        print(len(all_cells))
