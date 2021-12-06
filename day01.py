def part1(measures: list[int]) -> int:
    prev = None
    increases = 0
    for cur in measures:
        if prev and cur > prev:
            increases += 1
        prev = cur
    return increases

def part2(measures: list[int]) -> int:
    cur = sum(measures[:3])
    prev = cur
    increases = 0
    for i in range(3, len(measures)):
        cur += measures[i] - measures[i - 3]
        if cur > prev:
            increases += 1
        prev = cur
    return increases

with open('day01.txt') as f:
    measures = [int(x) for x in f]
    print(f'Part 1: {part1(measures)}')
    print(f'Part 2: {part2(measures)}')