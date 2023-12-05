with open("inputs/02_test.txt", "r") as File:
    lines = File.readlines()

max_color = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

ans = 0
for line in lines:
    colon = line.index(":")
    game_id = int(line[5:colon])
    sets = line[colon + 1:].split(";")
    is_possible = True
    for set in sets:
        draws = set.split(",")
        for draw in draws:
            num, color = draw.split()
            if int(num) > max_color[color]:
                is_possible = False
                break
        if not is_possible:
            break
    if is_possible:
        ans += game_id
print(ans)
