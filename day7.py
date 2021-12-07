with open("input7.txt") as f:
    inp = [int(n) for n in f.read().strip().split(",")]

part1, part2 = float("inf"), float("inf")

for pos in range(min(inp), max(inp)):

    diffs = [abs(pos - i) for i in inp]
    sums = [(n * (n + 1)) / 2 for n in diffs]

    part1 = min(part1, sum(diffs))
    part2 = min(part2, sum(sums))

print(part1, int(part2))
