from collections import Counter

with open("input6.txt") as f:
    nums = [int(n) for n in f.read().strip().split(",")]


track = Counter(nums)

for day in range(256):
    new = track[0]
    for i in range(8):
        track[i] = track[i + 1]
    track[8] = new
    track[6] += new


print(sum(track.values()))
