grid = [[int(x) for x in line]
        for line in open('day11.txt').read().splitlines()]
n = len(grid)
m = len(grid[0])
adjacent = [(1, 0), (1, 1), (0, 1), (-1, 1),
            (-1, 0), (-1, -1), (0, -1), (1, -1)]


def step() -> int:
    for i in range(n):
        for j in range(m):
            grid[i][j] += 1

    flashes = 0
    stop = False
    while not stop:
        stop = True
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 9:
                    flashes += 1
                    stop = False
                    for ii, jj in adjacent:
                        ii += i
                        jj += j
                        inside = ii >= 0 and ii < n and jj >= 0 and jj < m 
                        if inside and grid[ii][jj] > 0:
                            grid[ii][jj] += 1
                    grid[i][j] = 0
    return flashes


flashes = 0
steps = 0
while True:
    this_flash = step()
    steps += 1
    flashes += this_flash
    if this_flash == n * m:
        print(f'Part 2: {steps}')
        break
    if steps == 100:
        print(f'Part 1: {flashes}')
