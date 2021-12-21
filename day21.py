import functools

A_START, B_START = 6, 9

def roll():
    global die, rolls
    ret = die
    rolls += 1
    die += 1
    if die > 100:
        die = 1
    return ret

rolls = 0
die = 1
a, b = A_START, B_START
a_score, b_score = 0, 0
while True:
    a = (a - 1 + roll() + roll() + roll()) % 10 + 1
    a_score += a
    if a_score >= 1000:
        break
    b = (b - 1 + roll() + roll() + roll()) % 10 + 1
    b_score += b
    if b_score >= 1000:
        break

print(f'Part 1: {min(a_score, b_score) * rolls}')

@functools.cache
def dp(a: int, b: int, a_score: int, b_score: int, a_turn: bool) -> tuple[int, int]:
    if a_score >= 21:
        return 1, 0
    elif b_score >= 21:
        return 0, 1
    
    a_ways, b_ways = 0, 0
    for roll, ways in ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)):
        if a_turn:
            new_a = (a - 1 + roll) % 10 + 1
            new_b = b
            new_a_score = a_score + new_a
            new_b_score = b_score
        else:
            new_a = a
            new_b = (b - 1 + roll) % 10 + 1
            new_a_score = a_score
            new_b_score = b_score + new_b
        a_res, b_res = dp(new_a, new_b, new_a_score, new_b_score, not a_turn)
        a_ways += a_res * ways
        b_ways += b_res * ways
    return a_ways, b_ways

print(f'Part 2: {max(dp(A_START, B_START, 0, 0, True))}')