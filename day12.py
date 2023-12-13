from collections import defaultdict
with open("inputs/12.txt", "r") as File:
    corrupts1, groupings1 = [], []
    corrupts2, groupings2 = [], []
    for line in File:
        s1, s2 = line[:-1].split()
        corrupts1.append(s1)
        groupings1.append([int(group) for group in s2.split(',')])
        s1 += '?'
        s1 = 5 * s1
        corrupts2.append(s1[:-1])
        groupings2.append([int(group) for group in s2.split(',')]*5)

def count_arrangements(corrupt, grouping):
    combs = {0: 1}
    n = len(corrupt)
    for k in grouping:
        new_combs = defaultdict(int)
        for start, count in combs.items():
            is_done = False #true if done with this grouping
            for i in range(start, n-k+1):
                if is_done:
                    break
                s = corrupt[i:i+k]
                if s[0] == '#':
                    is_done = True
                if '.' in s:
                    continue
                if (i+k) < n and corrupt[i+k] == '#':
                    continue
                new_combs[i+k+1] += count
        combs = new_combs.copy()
    for i in combs:
        if '#' in corrupt[i:]:
            combs[i] = 0
    return(sum(combs.values()))

ans_p1 = 0
for i, (corrupt, grouping) in enumerate(zip(corrupts1, groupings1)):
    ans_p1 += count_arrangements(corrupt, grouping)

ans_p2 = 0
for corrupt, grouping in zip(corrupts2, groupings2):
    ans_p2 += count_arrangements(corrupt, grouping)

print(f"Part 1 answer: {ans_p1}")
print(f"Part 2 answer: {ans_p2}")
