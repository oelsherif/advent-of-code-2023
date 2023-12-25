import numpy as np
from scipy.optimize import least_squares

with open("inputs/24.txt", "r") as File:
    lines = [line[:-1] for line in File]

positions = []
velocities = []
for line in lines:
    position, velocity = line.split('@')
    pos = [int(p) for p in position.split(',')]
    vel = [int(v) for v in velocity.split(',')]
    positions.append(pos)
    velocities.append(vel)

n = len(lines)

def equations(vars, xs, vxs, ys, vys, zs, vzs):
    x0, vx0, y0, vy0, z0, vz0 = vars[:6]
    ts = vars[6:]

    residuals = np.zeros(3*n)
    for i in range(n):
        residuals[i] = x0 + vx0*ts[i] - xs[i] - vxs[i]*ts[i]
        residuals[n+i] = y0 + vy0*ts[i] - ys[i] - vys[i]*ts[i]
        residuals[2*n+i] = z0 + vz0*ts[i] - zs[i] - vzs[i]*ts[i]
    return residuals

xs = np.array([pos[0] for pos in positions])
ys = np.array([pos[1] for pos in positions])
zs = np.array([pos[2] for pos in positions])
vxs = np.array([vel[0] for vel in velocities])
vys = np.array([vel[1] for vel in velocities])
vzs = np.array([vel[2] for vel in velocities])

#guess = np.zeros(6 + n)
guess = np.empty(6 + n)
guess.fill(100000000000000)
guess[1] = 0
guess[3] = 0
guess[5] = 0

np.set_printoptions(suppress=True, formatter={'float_kind':'{:f}'.format})

result = least_squares(equations, guess, args=(xs, vxs, ys, vys, zs, vzs))
print(result.x)
print('{:f}'.format(result.x[0] + result.x[2] + result.x[4]))
