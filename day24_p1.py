with open("inputs/24.txt", "r") as File:
    lines = [line[:-1] for line in File]

positions = []
velocities = []
for line in lines:
    position, velocity = line.split('@')
    px, py, pz = [int(p) for p in position.split(',')]
    vx, vy, vz = [int(v) for v in velocity.split(',')]
    positions.append((px, py, pz))
    velocities.append((vx, vy, vz))


def is_cross_2D(pos1, vel1, pos2, vel2):
    x0_1, y0_1, z0_1 = pos1
    vx_1, vy_1, vz_1 = vel1
    x0_2, y0_2, z0_2 = pos2
    vx_2, vy_2, vz_2 = vel2
    if vx_2*vy_1 == vy_2 * vx_1:
        #print("parallel")
        return False
    t2 = (y0_2 * vx_1 - y0_1 * vx_1 + x0_1 * vy_1 - x0_2 * vy_1) / (vx_2 * vy_1 - vy_2 * vx_1)
    t1 = (x0_2 - x0_1 + vx_2 * t2) / vx_1
    if t1 < 0 or t2 < 0:
        #print("past")
        return False
    x = x0_1 + vx_1 * t1
    y = y0_1 + vy_1 * t1
    #print(x, y)
    if x < start or x > end:
        return False
    if y < start or y > end:
        return False
    return True

n = len(positions)
test_min, test_max = 7, 27
real_min, real_max = 200000000000000, 400000000000000

test = False
if (test == True):
    start, end = test_min, test_max
else:
    start, end = real_min, real_max

crosses = 0
for i in range(n):
    pos1, vel1 = positions[i], velocities[i]
    for j in range(i+1, n):
        pos2, vel2 = positions[j], velocities[j]
        crosses += is_cross_2D(pos1, vel1, pos2, vel2)

ans_p1 = crosses
print(f"Part 1 answer: {ans_p1}")
