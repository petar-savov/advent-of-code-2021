from collections import Counter

with open("input14.txt") as f:
    t, ins = f.read().strip().split("\n\n")

ins = dict(i.split(r" -> ") for i in ins.split("\n"))
pairs = Counter(map(str.__add__, t[:-1], t[1:]))
track = Counter(t)

for _ in range(40):
    for p, c in pairs.copy().items():
        middle = ins[p]
        pairs[p] -= c
        pairs[p[0] + middle] += c
        pairs[middle + p[1]] += c
        track[middle] += c

print(max(track.values()) - min(track.values()))
