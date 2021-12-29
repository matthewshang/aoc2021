from bisect import bisect_left, bisect_right
from collections import defaultdict


class Step:
    def __init__(self, rep: str):
        op, where = rep.split()
        x, y, z = where.split(',')
        self.x_min, self.x_max = map(int, x[2:].split('..'))
        self.y_min, self.y_max = map(int, y[2:].split('..'))
        self.z_min, self.z_max = map(int, z[2:].split('..'))
        self.op = op


steps = [Step(line) for line in open('day22.txt').read().splitlines()]

grid = defaultdict(bool)
for step in steps:
    x_min = max(-50, step.x_min)
    x_max = min(50, step.x_max)
    y_min = max(-50, step.y_min)
    y_max = min(50, step.y_max)
    z_min = max(-50, step.z_min)
    z_max = min(50, step.z_max)

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                grid[x, y, z] = step.op == 'on'

on = print(f'Part 1: {sum(grid.values())}')

xs = sorted([s.x_min for s in steps] + [s.x_max + 1 for s in steps])
ys = sorted([s.y_min for s in steps] + [s.y_max + 1 for s in steps])
zs = sorted([s.z_min for s in steps] + [s.z_max + 1 for s in steps])
n = len(xs)
grid = [False] * (n * n * n)
for s in steps:
    x_min = bisect_left(xs, s.x_min)
    x_max = bisect_right(xs, s.x_max)
    y_min = bisect_left(ys, s.y_min)
    y_max = bisect_right(ys, s.y_max)
    z_min = bisect_left(zs, s.z_min)
    z_max = bisect_right(zs, s.z_max)
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            for z in range(z_min, z_max):
                grid[x * n * n + y * n + z] = s.op == 'on'
on = 0
for x in range(n - 1):
    for y in range(n - 1):
        for z in range(n - 1):
            on += grid[x * n * n + y * n + z] * \
                (xs[x + 1] - xs[x]) * (ys[y + 1] - ys[y]) * (zs[z + 1] - zs[z])
print(f'Part 2: {on}')
