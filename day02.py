lines = open('day02.txt').readlines()

position, depth = 0, 0
for line in lines:
    direction, X = line.split()
    X = int(X)
    match direction:
        case 'forward': position += X
        case 'down': depth += X
        case 'up': depth -= X
print(f'Part 1: {position * depth}')

position, depth, aim = 0, 0, 0
for line in lines:
    direction, X = line.split()
    X = int(X)
    match direction:
        case 'forward':
            position += X
            depth += aim * X
        case 'down': aim += X
        case 'up': aim -= X
print(f'Part 2: {position * depth}')