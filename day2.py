with open("input2.txt") as f:
    inp = [line.strip() for line in f.readlines()]

# part 1
h, d = 0, 0

for line in inp:
    x = int(line[-1])
    if line.startswith("down"):
        d += x
    elif line.startswith("up"):
        d -= x
    else:
        h += x

print(h * d)

# part 2
h, d, aim = 0, 0, 0

for line in inp:
    x = int(line[-1])
    if line.startswith("down"):
        aim += x
    elif line.startswith("up"):
        aim -= x
    else:
        h += x
        d += aim * x

print(h * d)
