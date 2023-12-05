from collections import defaultdict
from copy import deepcopy
with open("inputs/05.txt", "r") as File:
    lines = [line[:-1] for line in File]

seeds = [int(seed) for seed in lines[0][6:].split()]
seed_ranges = [ [seeds[i], seeds[i] + seeds[i+1]] for i in range(0, len(seeds), 2)]
stages = defaultdict(list)

stage = -1
for line in lines[2:]:
    if "map" in line:
        stage += 1
        continue
    if not line:
        continue
    stages[stage].append([int(num) for num in line.split()])

for maps in stages.values():
    new_seed_ranges = []
    while seed_ranges:
        seed_start, seed_end = seed_ranges.pop()
        if seed_start >= seed_end:
            continue
        for map in maps:
            map_size = map[2]
            map_start = map[1]
            map_end = map_start + map_size
            dest_start = map[0]
            if map_start >= seed_end or map_end <= seed_start:
                continue

            if map_start >= seed_start and map_end <= seed_end:
                new_seed_ranges.append( [dest_start, dest_start + map_size])
                seed_ranges.append( [seed_start, map_start] )
                seed_ranges.append( [map_end, seed_end])
            elif map_start < seed_start and map_end > seed_end:
                new_seed_ranges.append( [dest_start + seed_start - map_start, dest_start + seed_end - map_start])
            elif map_start >= seed_start:
                new_seed_ranges.append( [dest_start, dest_start + seed_end - map_start])
                seed_ranges.append( [seed_start, map_start])
            elif map_end <= seed_end:
                new_seed_ranges.append( [dest_start + seed_start - map_start, dest_start + map_size])
                seed_ranges.append( [map_end, seed_end])
            break
        else:
            new_seed_ranges.append([seed_start, seed_end])
    seed_ranges = deepcopy(new_seed_ranges)

print(min([range[0] for range in seed_ranges]))