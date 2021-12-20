import numpy as np
from scipy.ndimage import convolve

with open("input20.txt") as f:
    alg, img = f.read().split("\n\n")

alg = np.array([1 if c == "#" else 0 for c in alg])
img = [[1 if c == "#" else 0 for c in line] for line in img.split()]
img = np.array(img)
img = np.pad(img, 51, constant_values=0)

k = 2 ** np.arange(9).reshape(3, 3)

for i in range(50):
    img = alg[convolve(img, k)]
    if i + 1 in (2, 50):
        print(img.sum())
