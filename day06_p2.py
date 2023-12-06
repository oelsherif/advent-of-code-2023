from math import sqrt
with open("inputs/06.txt", "r") as File:
    lines = File.readlines()

## With T as time, D as distance, and t is the time where we would exactly run distance D
## we solve for t in: t * (T-t) = D
## t = (T ± sqrt(T^2 - 4D))/2 gets us two solutions, where the range between them would win.

T = int("".join(lines[0].split()[1:]))
D = int("".join(lines[1].split()[1:]))

t1 = int( (T - sqrt(T*T - 4*D)) // 2 )
t2 = T - t1
ans = t2 - t1 - 1

print(ans)
