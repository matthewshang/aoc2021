positions = [int(x) for x in open('day07.txt').readline().split(',')]
n = len(positions)
positions = sorted(positions)
median = positions[n // 2] if n % 2 == 0 else (positions[n // 2] + positions[n // 2 + 1]) / 2
fuel = sum(abs(x - median) for x in positions)
print(f'Part 1: {fuel}')

fuel = min(sum(abs(x - m) * (abs(x - m) + 1) // 2 for x in positions) for m in range(max(positions) + 1))
print(f'Part 2: {fuel}')