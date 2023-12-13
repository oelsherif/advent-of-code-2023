with open("inputs/13.txt", "r") as File:
    lines = [line[:-1] for line in File]

def reflection_index(grid):
    n = len(grid)
    vert_flip = grid[::-1]
    for i in range(1, n):
        for row1, row2 in zip(grid[i:], vert_flip[n-i:]):
            if row1 != row2:
                break
        else:
            return i
    return 0

def imperfect_reflection_index(grid):
    n = len(grid)
    vert_flip = grid[::-1]
    for i in range(1, n):
        n_smidges = 0
        for row1, row2 in zip(grid[i:], vert_flip[n-i:]):
            if (smidges := string_diff(row1, row2)) > 1:
                break
            n_smidges += smidges
        else:
            if n_smidges == 1:
                return i
    return 0

def transpose(grid):
    return [ '.'.join([row[i] for row in grid]) for i in range(len(grid[0]))]

def string_diff(s1, s2):
    """return number of different characters between two strings of equal length"""
    d = 0
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            d += 1
    return d

grids = []
i = 0
n = len(lines)
while i < n:
    if not lines[i]:
        i += 1
        continue
    j = i
    while j < n:
        if not lines[j]:
            break
        j += 1 
    grids.append(lines[i:j])
    i = j + 1

ans_p1 = 0
for grid in grids:
    ans_p1 += 100*reflection_index(grid)
    ans_p1 += reflection_index(transpose(grid))
    
ans_p2 = 0
for grid in grids:
    ans_p2 += 100*imperfect_reflection_index(grid)
    ans_p2 += imperfect_reflection_index(transpose(grid))

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
