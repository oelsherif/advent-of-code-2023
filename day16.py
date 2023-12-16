from collections import defaultdict

with open("inputs/16.txt", "r") as File:
    grid = [line[:-1] for line in File]

n_rows = len(grid)
n_cols = len(grid[0])

def in_grid(x, y) -> bool:
    if x < 0 or x >= n_cols or y < 0 or y >= n_rows:
        return False
    return True

dirs = ['N', 'E', 'S', 'W']

resulting_dirs = {
    '.': {dir: [dir] for dir in dirs},
    '/': {'E': ['N'], 'N': ['E'], 'S': ['W'], 'W': ['S']},
    '\\': {'E': ['S'], 'S': ['E'], 'W': ['N'], 'N': ['W']},
    '|': {
        'E': ['N', 'S'],
        'W': ['N', 'S'],
        'N': ['N'],
        'S': ['S']
    },
    '-': {
        'E': ['E'],
        'W': ['W'],
        'N': ['E', 'W'],
        'S': ['E', 'W']
    }
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

def mark(symbol, dir):
    """Give a mark of how each tile was visited"""
    if symbol == '.':
        if dir in 'NS':
            return '|'
        else:
            return '-'
    if symbol in '|-':
        return '.'
    if symbol == '/':
        if dir in 'ES':
            return 'J'
        else:
            return 'F'
    if symbol == '\\':
        if dir in 'EN':
            return '7'
        else:
            return 'L'

def count_energized(x0, y0, dir0):
    visited = defaultdict(list)
    visited[(x0, y0)].append(mark(grid[y0][x0], dir0))
    beams = []
    for dir in resulting_dirs[grid[y0][x0]][dir0]:
        beams.append((x0, y0, dir))
    while True:
        new_beams = []
        for x, y, dir in beams:
            new_x, new_y = new_pos(x, y, dir)
            if not in_grid(new_x, new_y):
                continue
            new_symbol = grid[new_y][new_x]
            if (new_mark:=mark(new_symbol, dir)) in visited[(new_x, new_y)]:
                continue
            visited[(new_x,new_y)].append(new_mark)
            for new_dir in resulting_dirs[grid[new_y][new_x]][dir]:
                new_beams.append((new_x,new_y,new_dir))
        if not new_beams:
            break
        beams = new_beams.copy()
    return len(visited.keys())

ans_p1 = count_energized(0, 0, 'E')
print(f"Part 1 answer: {ans_p1}")

ans_p2 = 0
for x0 in range(n_cols):
    energized1 = count_energized(x0, 0, 'S')
    energized2 = count_energized(x0, n_rows-1, 'N')
    ans_p2 = max(ans_p2, energized1, energized2)
for y0 in range(n_rows):
    energized1 = count_energized(0, y0, 'E')
    energized2 = count_energized(n_cols-1, y0, 'W')
    ans_p2 = max(ans_p2, energized1, energized2)
print(f"Part 2 answer: {ans_p2}")
