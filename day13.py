import numpy as np
import matplotlib.pyplot as plt

with open("input13.txt") as f:
    nums, folds = f.read().split("\n\n")

nums = [[int(n) for n in line.split(",")] for line in nums.split("\n")]
folds = [
    (line.split(r"=")[0][-1], int(line.split(r"=")[1]))
    for line in folds.strip().split("\n")
]

# could also be done with np.flip
for fdir, faxis in folds:
    new = []
    for x, y in nums:
        if fdir == "x":
            if x < faxis:
                new.append((x, y))
            elif x > faxis:
                newx = faxis - (x - faxis)
                new.append((newx, y))
        if fdir == "y":
            if y < faxis:
                new.append((x, y))
            elif y > faxis:
                newy = faxis - (y - faxis)
                new.append((x, newy))
    nums = new


xmax, ymax = max(n[0] for n in nums), max(n[1] for n in nums)
arr = np.zeros((ymax + 1, xmax + 1))
for x, y in nums:
    arr[y, x] = 1

plt.imshow(arr)
plt.show()
