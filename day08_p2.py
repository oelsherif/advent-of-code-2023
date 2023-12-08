from math import lcm
with open("inputs/08.txt", "r") as File:
    lines = File.readlines()

directions = lines[0][:-1]
cycle_length = len(directions)
adjs = {line[0:3]: [line[7:10], line[12:15]] for line in lines[2:]}
starts = [loc for loc in adjs.keys() if loc[2] == 'A']
dir_index = {"L": 0, "R": 1}

##### NOT SUPER HAPPY WITH THIS APPROACH
##### Works for the way the input file is generated, but not a general approach
#I wanted to catch the loops, so I printed when you'd reach targets from each starting point
#Turns out that for each starting point, you can only reach one target
#and you reach it after a certain number of cycles, at the exact end of the cycle
#The commented code got me that information, so I used it to write the actual solution
# for start in starts:
#     current = start
#     steps, cycle_number, cycle_step = 0, 0, 0
#     while True:
#         direction = dir_index[directions[cycle_step]]
#         current = adjs[current][direction]
#         if cycle_number >= 500:
#             break
#         steps += 1
#         cycle_number = steps // cycle_length
#         cycle_step = steps % cycle_length
#         if current[2] == 'Z':
#             print(start, current, cycle_number, cycle_step)

cycles_to_target = []
for start in starts:
    current = start
    steps, cycle_number, cycle_step = 0, 0, 0
    while True:
        direction = dir_index[directions[cycle_step]]
        current = adjs[current][direction]
        steps += 1
        cycle_number = steps // cycle_length
        cycle_step = steps % cycle_length
        if current[2] == 'Z':
            cycles_to_target.append(cycle_number)
            break

print(cycles_to_target)
#Now we just have to find the first cycle they all reach a target
#And multiply it by the number of steps per cycle
ans = cycle_length * lcm(*cycles_to_target)
print(ans)