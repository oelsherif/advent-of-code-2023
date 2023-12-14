from copy import deepcopy
with open("inputs/14.txt", "r") as File:
    grid = [line[:-1] for line in File]

def transpose(grid):
    return [ ''.join([row[i] for row in grid]) for i in range(len(grid[0]))]

def flip(grid):
    """flips grid horizontally"""
    return [row[::-1] for row in grid]

def tilt_row(row):
    """tilts row to the west"""
    n = len(row)
    i = 0
    while i < n:
        if row[i] == '#':
            i += 1
            continue
        j = i
        while j < n:
            if row[j] == '#':
                break
            j += 1
        s = row[i:j]
        n_hashes = s.count('O')
        s = 'O' * n_hashes + '.' * (len(s) - n_hashes)
        row = row[:i] + s + row[j:]
        i = j + 1
    return row
        
def tilt_west(grid):
    return [tilt_row(row) for row in grid]

def tilt_east(grid):
    return flip(tilt_west(flip(grid)))

def tilt_north(grid):
    return transpose(tilt_west(transpose(grid)))

def tilt_south(grid):
    return transpose(tilt_east(transpose(grid)))

def total_load(grid):
    load = 0
    for i, row in enumerate(grid):
        load += (len(grid)-i) * row.count('O')
    return load

def cycle(grid):
    return tilt_east(tilt_south(tilt_west(tilt_north(grid))))

ans_p1 = total_load(tilt_north(grid))

#PLAN FOR PART 2:
#DO MATH TO GET BILLION'S CYCLE
#SAVE GRID AFTER n_test CYCLES, COPARE AFTER EACH FUTURE CYCLE TO SEE WHEN IT WOULD HAPPEN AGAIN
#GET LENGTH OF LOOP (len_loop)
#SEE HOW FAR IN THE LOOP THE BILLION IS index_correct = (Billion - n_test) % len_loop
#Calculate total_load of index_correct

n_test = 201
for i in range(n_test):
    grid = cycle(grid)

grid_test = deepcopy(grid)
for i in range(n_test):
    grid = cycle(grid)
    if grid == grid_test:
        break

len_loop = i + 1
if len_loop == n_test:
    print("n_test is too small")
else:
    print(f'Length of Loop is {len_loop}')

wanted = 10**9
index_correct = (wanted - n_test) % len_loop
for i in range(index_correct):
    grid_test = cycle(grid_test)

ans_p2 = total_load(grid_test)

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
