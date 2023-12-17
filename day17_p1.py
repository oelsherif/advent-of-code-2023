import time
with open("inputs/17.txt", "r") as File:
    grid = [[int(char) for char in line[:-1]] for line in File]

n_rows = len(grid)
n_cols = len(grid[0])

def in_grid(x: int, y: int) -> bool:
    if x < 0 or x >= n_cols or y < 0 or y >= n_rows:
        return False
    return True

dirs = ['N', 'E', 'S', 'W']

opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

def new_pos(x: int, y: int, dir: str) -> (int, int):
    if dir == 'E':
        return x+1, y
    if dir == 'W':
        return x-1, y
    if dir == 'N':
        return x, y-1
    if dir == 'S':
        return x, y+1

def get_mark(old_mark: str, dir:str) -> str:
    count_dir = old_mark.count(dir)
    if count_dir > 2:
        return 'X'
    if count_dir == 0:
        return dir
    return old_mark + dir

def choose(mark1: str, heat1: int, mark2: str, heat2: str):
    """
    Chooses whether one of the two sets is superior to the other 
    returns 0 if old is better
    returns 1 if new is better
    returns 2 if neither can replace the other
    """
    if mark1 in mark2 and heat1 <= heat2:
        return 0
    if mark2 in mark1 and heat2 <= heat1:
        return 1
    return 2

best_grid = [[[] for _ in range(n_cols)] for _ in range(n_rows)]

t1 = time.time()

x0, y0, mark0, heat0 = 0, 0, '', 0
currents = [(x0, y0, mark0, heat0)]
while True:
    new_currents = []
    did_anything_change = False
    for x, y, mark, heat in currents:
        for dir in dirs:
            if mark and dir == opposite[mark[-1]]:
                continue
            new_x, new_y = new_pos(x, y, dir)
            if not in_grid(new_x, new_y):
                continue
            new_heat = heat + grid[new_y][new_x]
            new_mark = get_mark(mark, dir)
            if new_mark == 'X':
                continue
            if not best_grid[new_y][new_x]:
                best_grid[new_y][new_x].append((new_mark, new_heat))
                new_currents.append((new_x, new_y, new_mark, new_heat))
                did_anything_change = True
                continue
            new_list = []
            for old_mark, old_heat in best_grid[new_y][new_x]:
                choice = choose(old_mark, old_heat, new_mark, new_heat)
                is_change = True
                if choice == 0:
                    is_change = False
                    break
                if choice == 2:
                    new_list.append((old_mark, old_heat))
            if is_change:
                did_anything_change = True
                new_list.append((new_mark, new_heat))
                best_grid[new_y][new_x] = new_list.copy()
                new_currents.append((new_x, new_y, new_mark, new_heat))
    if not did_anything_change:
        break
    currents = new_currents.copy()

t2 = time.time()
print(t2 - t1)
ans_p1 = min(t[1] for t in best_grid[-1][-1])
print(f"Part 1 answer: {ans_p1}")
