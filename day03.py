lines = open('day03.txt').read().splitlines()


def count_has_ones(vals: list[str], bit: int) -> int:
    count = 0
    for v in vals:
        if v[bit] == '1':
            count += 1
    return count


n = len(lines[0])
m = len(lines)
one_count = [count_has_ones(lines, i) for i in range(n)]

epsilon, gamma = 0, 0
for i in range(n):
    if one_count[i] > m - one_count[i]:
        gamma += 1 << (n - i - 1)
    else:
        epsilon += 1 << (n - i - 1)
print(f'Part 1: {gamma * epsilon}')

vals = lines[:]
for i in range(n):
    ones = count_has_ones(vals, i)
    keep = '1' if ones >= len(vals) - ones else '0'
    vals[:] = [val for val in vals if val[i] == keep]
assert len(vals) == 1
oxygen = int(vals[0], 2)

vals = lines[:]
for i in range(n):
    ones = count_has_ones(vals, i)
    keep = '0' if len(vals) - ones <= ones else '1'
    vals[:] = [val for val in vals if val[i] == keep]
    if len(vals) == 1:
        break
assert len(vals) == 1
co2 = int(vals[0], 2)

print(f'Part 2: {oxygen * co2}')
