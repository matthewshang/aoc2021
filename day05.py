from itertools import chain

lines = open('day05.txt').read().splitlines()

grid = [[0] * 1000 for _ in range(1000)]
grid_all = [[0] * 1000 for _ in range(1000)]
for line in lines:
    line = line.split(' ')
    x1, y1 = [int(x) for x in line[0].split(',')]
    x2, y2 = [int(x) for x in line[2].split(',')]
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            grid[x1][y] += 1
            grid_all[x1][y] += 1
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            grid[x][y1] += 1
            grid_all[x][y1] += 1
    else:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for i in range(x2 - x1 + 1):
            j = i if y1 < y2 else -i
            grid_all[x1 + i][y1 + j] += 1

count = sum(c > 1 for c in chain.from_iterable(zip(*grid)))
print(f'Part 1: {count}')
count = sum(c > 1 for c in chain.from_iterable(zip(*grid_all)))
print(f'Part 2: {count}')