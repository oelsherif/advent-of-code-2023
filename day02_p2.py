import numpy as np
with open("inputs/02.txt", "r") as File:
    lines = File.readlines()

ans = 0
for line in lines:
    max_color = {
    "red": 0,
    "green": 0,
    "blue": 0,
    }

    colon = line.index(":")
    # game_id = int(line[5:colon])
    sets = line[colon + 1:].split(";")
    is_possible = True
    for set in sets:
        draws = set.split(",")
        for draw in draws:
            num, color = draw.split()
            if int(num) > max_color[color]:
                max_color[color] = int(num)
    ans += np.prod(list(max_color.values()))
print(ans)
