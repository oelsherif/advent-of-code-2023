from collections import defaultdict
with open("inputs/05.txt", "r") as File:
    lines = [line[:-1] for line in File]

seeds = [int(seed) for seed in lines[0][6:].split()]
stages = defaultdict(list)

stage = -1
for line in lines[2:]:
    if "map" in line:
        stage += 1
        continue
    if not line:
        continue
    stages[stage].append([int(num) for num in line.split()])

for i, seed in enumerate(seeds):
    for maps in stages.values():
        for map in maps:
            start = map[1]
            end = start + map[2]
            dest_start = map[0]
            if seed in range(start,end):
                seed = dest_start + seed - start
                seeds[i] = seed
                break

print(min(seeds))
