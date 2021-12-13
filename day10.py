lines = open('day10.txt').read().splitlines()

corrupt_value = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_value = {')': 1, ']': 2, '}': 3, '>': 4}
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

score = 0
incompletes = []
for line in lines:
    stack = []
    for c in line:
        if c in pairs:
            stack.append(pairs[c])
        else:
            if not stack or stack[-1] != c:
                score += corrupt_value[c]
                break
            else:
                stack.pop()
    else:
        incomplete_score = 0
        while stack:
            incomplete_score = incomplete_score * \
                5 + incomplete_value[stack.pop()]
        incompletes.append(incomplete_score)

print(f'Part 1: {score}')
incompletes.sort()
print(f'Part 2: {incompletes[len(incompletes) // 2]}')
