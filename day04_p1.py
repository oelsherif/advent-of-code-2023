with open("inputs/04.txt", "r") as File:
    lines = File.readlines()

ans = 0
for line in lines:
    colon = line.index(":")
    winning, owned = line[colon + 1:].split("|")
    winning_nums = set(winning.split())
    owned_nums = set(owned.split())
    num_wins = len(winning_nums & owned_nums)
    if num_wins:
        ans += 2 ** (num_wins - 1)

print(ans)