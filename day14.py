from collections import Counter

lines = open('day14.txt').read().splitlines()

rules = {}
for rule in lines[2:]:
    pair, _, insertion = rule.split(' ')
    rules[tuple(pair)] = insertion


def process(start: str, steps: int) -> int:
    count = Counter(start)
    template = Counter(zip(start, start[1:]))
    for _ in range(steps):
        next_template = Counter()
        for pair, num in template.items():
            insertion = rules[pair]
            next_template[pair[0], insertion] += num
            next_template[insertion, pair[1]] += num
            count[insertion] += num
        template = next_template
    return max(count.values()) - min(count.values())


print(f'Part 1: {process(lines[0], 10)}')
print(f'Part 2: {process(lines[0], 40)}')
