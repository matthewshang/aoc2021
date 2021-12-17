from heapq import heappush, heappop


def shortest_path(grid: dict[tuple[int, int], int], n: int, m: int) -> int:
    dist = {}
    for i in range(n):
        for j in range(m):
            dist[i, j] = 10 ** 9
    dist[0, 0] = 0

    pq = [(0, 0, 0)]
    while pq:
        path_len, i, j = heappop(pq)
        if path_len == dist[i, j]:
            if i == n - 1 and j == m - 1:
                break
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                inside = ni >= 0 and ni < n and nj >= 0 and nj < m
                if inside and path_len + grid[ni, nj] < dist[ni, nj]:
                    dist[ni, nj] = path_len + grid[ni, nj]
                    heappush(pq, (dist[ni, nj], ni, nj))
    return dist[n - 1, m - 1]


lines = open('day15.txt').read().splitlines()
grid = {}
n = len(lines)
m = len(lines[0])
for i in range(n):
    for j in range(m):
        grid[i, j] = int(lines[i][j])
        for gi in range(5):
            for gj in range(5):
                if gi > 0 or gj > 0:
                    ni, nj = gi * n + i, gj * m + j
                    grid[ni, nj] = (grid[i, j] + gi + gj - 1) % 9 + 1

print(f'Part 1: {shortest_path(grid, n, m)}')
print(f'Part 2: {shortest_path(grid, n * 5, m * 5)}')
