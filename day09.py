from heapq import nlargest
from collections import deque
from functools import reduce
from operator import mul

grid = [[int(x) for x in line]
        for line in open('day09.txt').read().splitlines()]
n = len(grid)
m = len(grid[0])


def low(row: int, col: int) -> bool:
    if row > 0 and grid[row - 1][col] <= grid[row][col]:
        return False
    if row < n - 1 and grid[row + 1][col] <= grid[row][col]:
        return False
    if col > 0 and grid[row][col - 1] <= grid[row][col]:
        return False
    if col < m - 1 and grid[row][col + 1] <= grid[row][col]:
        return False
    return True


def bfs(row: int, col: int) -> int:
    queue = deque([(row, col)])
    visited = set()
    size = 0
    while len(queue):
        row, col = queue.popleft()
        if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == 9:
            continue
        if (row, col) in visited:
            continue
        visited.add((row, col))
        size += 1
        queue.append((row - 1, col))
        queue.append((row + 1, col))
        queue.append((row, col - 1))
        queue.append((row, col + 1))
    return size


risk_sum = 0
basins = []
for i in range(n):
    for j in range(m):
        if low(i, j):
            risk_sum += grid[i][j] + 1
            basins.append(bfs(i, j))

print(f'Part 1: {risk_sum}')
print(f'Part 2: {reduce(mul, nlargest(3, basins), 1)}')
