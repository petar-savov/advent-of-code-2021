import re

with open("input17.txt") as f:
    inp = f.read()

xmin, xmax, ymin, ymax = [int(n) for n in re.findall("-?\d+", inp)]

print(ymin * (ymin + 1) // 2)


def simulate(vx, vy, px=0, py=0):
    if px > xmax or py < ymin:
        return 0
    if px >= xmin and py <= ymax:
        return 1
    return simulate(vx - (vx > 0), vy - 1, px + vx, py + vy)


vs = [simulate(vx, vy) for vx in range(xmax + 1) for vy in range(ymin, -ymin)]

print(sum(vs))
