lines = open('day13.txt').read().splitlines()
dots = set()
folds = []
for line in lines:
    if line.startswith('fold'):
        folds.append(line.split(' ')[2].split('='))
    elif line:
        dots.add(tuple(map(int, line.split(','))))

def do_fold(dots: set, where: int, dir: str) -> set:
    def flip_x(x: int, y: int) -> tuple[int, int]:
        return (x, y) if x < where else (2 * where - x, y)
    def flip_y(x: int, y: int) -> tuple[int, int]:
        return (x, y) if y < where else (x, 2 * where - y)
    return set(map(lambda p: flip_x(*p) if dir == 'x' else flip_y(*p), dots))

part1 = do_fold(dots, int(folds[0][1]), folds[0][0])
print(f'Part 1: {len(part1)}')

print('Part 2:')
for dir, where in folds:
    dots = do_fold(dots, int(where), dir)
cols = max(dot[0] for dot in dots) + 1
rows = max(dot[1] for dot in dots) + 1
for i in range(rows):
    for j in range(cols):
        print('#' if (j, i) in dots else '.', end='')
    print()
