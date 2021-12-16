import numpy as np
from scipy.ndimage import label

with open("input9.txt") as f:
    inp = [[int(x) for x in line.strip()] for line in f.readlines()]

# no numpy/scipy for part 1
risk_levels = 0
nrows, ncols = len(inp), len(inp[0])

for i in range(nrows):
    for j in range(ncols):
        pts = []
        if i + 1 < nrows:
            pts.append(inp[i + 1][j])
        if i - 1 >= 0:
            pts.append(inp[i - 1][j])
        if j + 1 < ncols:
            pts.append(inp[i][j + 1])
        if j - 1 >= 0:
            pts.append(inp[i][j - 1])
        if all([p > inp[i][j] for p in pts]):
            risk_levels += inp[i][j] + 1

print(risk_levels)

# part 2
labels, features = label(np.array(inp) != 9)
labels = labels.reshape(-1)
print(int(np.partition(np.bincount(labels, labels != 0), features - 3)[-3:].prod()))
