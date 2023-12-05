with open("inputs/04.txt", "r") as File:
    lines = File.readlines()

n = len(lines)
n_each = [1]*n
for i, line in enumerate(lines):
    copies = n_each[i]
    colon = line.index(":")
    winning, owned = line[colon + 1:].split("|")
    winning_nums = set(winning.split())
    owned_nums = set(owned.split())
    num_wins = len(winning_nums & owned_nums)
    start = i + 1
    end = min(start + num_wins, n)
    for j in range(start, end):
        n_each[j] += copies
print(sum(n_each))

