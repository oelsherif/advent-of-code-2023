from collections import defaultdict
with open("inputs/03.txt", "r") as File:
    lines = [line[:-1] for line in File]

digits = "0123456789"

m, n = len(lines), len(lines[0])
star_adjacents = defaultdict(list)
for i, line in enumerate(lines):
    j = 0
    while j < n:
        char = line[j]
        if char not in digits:
            j += 1
            continue
        k = j + 1
        while k < n:
            if line[k] in digits:
                k += 1
                continue
            break
        num = int(line[j:k])
        y_min = max(0, i-1)
        y_max = min(i+2, m)
        x_min = max(0, j - 1)
        x_max = min(k+1, n)
        for a in range(y_min, y_max):
            for b in range(x_min, x_max):
                if lines[a][b] == "*":
                    coordinate = str(a) + "," + str(b)
                    star_adjacents[coordinate].append(num)
        j = k

ans = 0
for adjacents in star_adjacents.values():
    if len(adjacents) == 2:
        ans += adjacents[0] * adjacents[1]
print(ans)

