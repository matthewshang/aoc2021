from collections import Counter

ages = map(int, open('day06.txt').read().split(','))
fish = Counter(ages)

def step():
    global fish
    next_fish = Counter()
    next_fish[6] += fish[0]
    next_fish[8] += fish[0]
    for i in range(1, 9):
        next_fish[i - 1] += fish[i]
    fish = next_fish.copy()

for _ in range(80):
    step()
print(f'Part 1: {sum(fish.values())}')

for _ in range(256 - 80):
    step()
print(f'Part 2: {sum(fish.values())}')