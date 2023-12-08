with open("inputs/08.txt", "r") as File:
    lines = File.readlines()

directions = lines[0][:-1]
directions_length = len(directions)
adjs = {line[0:3]: [line[7:10], line[12:15]] for line in lines[2:]}

current, target = "AAA", "ZZZ"

steps = 0
while current != target:
    direction = directions[steps % directions_length]
    if direction == "L":
        current = adjs[current][0]
    else:
        current = adjs[current][1]
    steps += 1
print(steps)