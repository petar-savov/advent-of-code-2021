from collections import Counter

with open("input10.txt") as f:
    inp = [line.strip() for line in f.readlines()]

opening, closing = r"([{<", r")]}>"
brackets = {k: v for k, v in zip(closing, opening)}
cost = {k: v for k, v in zip(closing, [3, 57, 1197, 25137])}

illegal, left_end = [], []

for line in inp:
    corrupted = False
    to_close = []  # unmatched characters
    for c in line:
        if c in opening:
            to_close.append(c)
            continue
        last = to_close.pop()
        if last != brackets[c]:
            corrupted = True
            illegal.append(c)
            break
    if not corrupted:
        left_end.append(to_close)

counter = Counter(illegal)
print(sum(cost[c] * counter[c] for c in closing))  # part 1

brackets = {v: k for k, v in brackets.items()}  # invert to opening:closing
point_value = {k: v for k, v in zip(closing, [1, 2, 3, 4])}

scores = []
for line in left_end:
    right_end = [brackets[c] for c in line[::-1]]
    score = 0
    for c in right_end:
        score = score * 5 + point_value[c]
    scores.append(score)

print(sorted(scores)[len(scores) // 2])  # part 2
