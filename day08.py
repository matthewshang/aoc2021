from itertools import permutations

lines = open('day08.txt').read().splitlines()

appears = 0
for line in lines:
    _, output = (seq.split() for seq in line.split('|'))
    for digit in output:
        if len(digit) in [2, 3, 4, 7]:
            print(digit)
            appears += 1
print(f'Part 1: {appears}')

digits = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}
alphabet = 'abcdefg'

ans = 0
for line in lines:
    pattern, output = (seq.split() for seq in line.split('|'))
    for perm in permutations(alphabet):
        transform = dict(zip(perm, alphabet))
        found = set()
        for digit in pattern:
            digit = ''.join(sorted(transform[x] for x in digit))
            if digit in digits:
                found.add(digits[digit])
            else:
                break

        if len(found) == 10:
            value = 0
            for digit in output:
                digit = ''.join(sorted(transform[x] for x in digit))
                value = value * 10 + digits[digit]
            ans += value
            break
print(f'Part 2: {ans}')