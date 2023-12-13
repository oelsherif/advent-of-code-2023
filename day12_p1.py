with open("inputs/12.txt", "r") as File:
    #lines = File.readlines()
    corrupts, groupings = [], []
    for line in File:
        s1, s2 = line[:-1].split()
        corrupts.append(list(s1))
        groupings.append([int(group) for group in s2.split(',')])

def reduce(s):
    """take condition and produe the corresponding grouping"""
    n = len(s)
    i = 0
    grouping = []
    while i < n:
        if s[i] != '#':
            i += 1
            continue
        j = i + 1
        while j < n:
            if s[j] != '#':
                break
            j += 1
        grouping.append(j-i)
        i = j
    return grouping

def check(s, grouping):
    """checks if the given condition matches the grouping"""
    return reduce(s) == grouping

def count_arrangements(loc_hash):
    if len(loc_hash) == n_missing_hash:
        new_corrupt = corrupt[:]
        for j in loc_hash:
            new_corrupt[loc_quest[j]] = '#'
        if check(new_corrupt, grouping):
            return 1
        return 0
    if not loc_hash:
        k = 0
    else:
        k = loc_hash[-1] + 1
    count = 0
    ceiling = n_quest - n_missing_hash + len(loc_hash) + 1
    for i in range(k, ceiling):
        count += count_arrangements(loc_hash + [i])
    return count

ans = 0
for corrupt, grouping in zip(corrupts, groupings):
    n_hash = corrupt.count('#')
    loc_quest = [i for i, char in enumerate(corrupt) if char == '?']
    n_quest = len(loc_quest)
    actual_n_hash = sum(grouping)
    n_missing_hash = actual_n_hash - n_hash
    ans += count_arrangements([])

print(ans)