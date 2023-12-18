from collections import defaultdict

with open("inputs/18.txt", "r") as File:
    lines = File.readlines()

direction = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

commands_p1 = []
commands_p2 = []
for line in lines:
    dir1, num1, p2 = line.split()
    dir2 = direction[p2[-2]]
    num2 = int(p2[2:-2], 16)
    commands_p1.append((dir1, int(num1)))
    commands_p2.append((dir2, num2))

def calculate_volume(commands):
    x, y = 0, 0
    map = defaultdict(list)
    for dir, num in commands:
        if dir in 'UD':
            if dir == 'U':
                y -= num
            else:
                y+= num
            continue
        if dir == 'R':
            new_x = x + num
            map[y].append((x, new_x))
        else:
            new_x = x - num
            map[y].append((new_x, x))
        x = new_x

    ys_sorted = sorted(map.keys())
    y_old = ys_sorted[0]
    xs_old = map[y_old]
    carried_size = sum([x2 - x1 + 1 for x1, x2 in xs_old])
    ans = carried_size
    for y in ys_sorted[1:]:
        #print(y, xs_old)
        #print(carried_size, sum([x2 - x1 + 1 for x1, x2 in xs_old]))
        ans += (y-y_old) * carried_size
        xs = sorted(map[y])
        for x1, x2 in xs:
            xs_old.sort()
            for i, x1_x2_old in enumerate(xs_old):
                x1_old, x2_old = x1_x2_old
                if x1 == x1_old and x2 == x2_old:
                    xs_old.pop(i)
                    carried_size -= (x2 - x1 + 1)
                    break
                elif x1 > x1_old and x2 < x2_old:
                    xs_old.pop(i)
                    xs_old.append((x1_old, x1))
                    xs_old.append((x2, x2_old))
                    carried_size -= (x2 - x1 - 1)
                    break
                elif x1 == x1_old and x2 < x2_old:
                    xs_old.pop(i)
                    xs_old.append((x2, x2_old))
                    carried_size -= (x2 - x1)
                    break
                elif x1 > x1_old and x2 == x2_old:
                    xs_old.pop(i)
                    xs_old.append((x1_old, x1))
                    carried_size -= (x2 - x1)
                    break
                elif x1 == x2_old:
                    if i < (len(xs_old) - 1) and x2 == xs_old[i+1][0]:
                        new_x2 = xs_old[i+1][1]
                        xs_old.pop(i)
                        xs_old.pop(i)
                        ans += x2 - x1 - 1
                        carried_size += x2 - x1 - 1
                        xs_old.append((x1_old, new_x2))
                    else:
                        xs_old.pop(i)
                        ans += x2 - x1
                        carried_size += x2 - x1
                        xs_old.append((x1_old, x2))
                    break
                elif x2 == x1_old:
                    xs_old.pop(i)
                    ans += x2 - x1
                    carried_size += x2 - x1
                    xs_old.append((x1, x2_old))
                    break
            else:
                ans += x2 - x1 + 1
                carried_size += x2 - x1 + 1
                xs_old.append((x1, x2))
        y_old = y   
    return(ans)

ans_p1 = calculate_volume(commands_p1)
print(f"Part 1 answer: {ans_p1}")
ans_p2 = calculate_volume(commands_p2)
print(f"Part 2 answer: {ans_p2}")