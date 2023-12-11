with open("inputs/11.txt", "r") as File:
    grid = [line[:-1] for line in File]

#Find Galaxies
m, n = len(grid[0]), len(grid)
galaxies = []
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == '#':
            galaxies.append([x, y])

empty_rows = [i for i, row in enumerate(grid) if row.count('#') == 0]
empty_columns = [i for i in range(m) if [row[i] for row in grid].count('#') == 0]
com_empty_rows, com_empty_columns = [], []
count = 0
for i in range(n):
    if i in empty_rows:
        count += 999999
    com_empty_rows.append(count)

count = 0
for i in range(m):
    if i in empty_columns:
        count += 999999
    com_empty_columns.append(count)

for galaxy in galaxies:
    galaxy[0] += com_empty_columns[galaxy[0]]
    galaxy[1] += com_empty_rows[galaxy[1]]

length = len(galaxies)
ans = 0
for i in range(length):
    for j in range(i+1, length):
        x0, y0 = galaxies[i]
        x1, y1 = galaxies[j]
        ans += abs(x1 - x0) + abs(y1 - y0)
print(ans)