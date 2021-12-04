import numpy as np

with open("input4.txt") as f:
    nums, *boards = f.read().strip().split("\n\n")

nums = [int(n) for n in nums.split(",")]

boards = [
    [[int(n) for n in line.split()] for line in board.split("\n")] for board in boards
]

boards = [np.array(board) for board in boards]


def check(board):
    if any(board.sum(0) == -5) or any(board.sum(1) == -5):
        return True
    return False


n_boards = len(boards)
wins = [0] * len(boards)

for n in nums:
    for i in range(n_boards):
        boards[i][boards[i] == n] = -1
        if wins[i] == 0 and check(boards[i]):
            res = n * (boards[i][boards[i] != -1].sum())
            wins[i] = 1
            if sum(wins) == 1:
                first = res
            if sum(wins) == n_boards:
                last = res
                break
    if sum(wins) == n_boards:
        break

print(first, last)
