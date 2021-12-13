lines = open('day04.txt').read().splitlines()

draws = [int(x) for x in lines[0].split(',')]
lines[:] = lines[1:]

boards = []
for i in range(len(lines) // 6):
    board = []
    for j in range(6):
        board += [int(x) for x in lines[i * 6 + j].split()]
    boards.append(board)

won = set()
for draw in draws:
    for idx, board in enumerate(boards):
        for i in range(25):
            if board[i] == draw:
                board[i] = -1

        win = False
        for row in range(5):
            if all(board[row * 5 + col] == -1 for col in range(5)):
                win = True
                break
        for col in range(5):
            if all(board[row * 5 + col] == -1 for row in range(5)):
                win = True
                break

        if win and idx not in won:
            won.add(idx)
            if len(won) == 1:
                score = draw * sum(filter(lambda x: x != -1, board))
                print(f'Part 1: {score}')
            elif len(won) == len(boards):
                score = draw * sum(filter(lambda x: x != -1, board))
                print(f'Part 2: {score}')
