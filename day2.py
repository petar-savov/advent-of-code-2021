with open("input2.txt") as f:
    inp = [line.strip() for line in f.readlines()]

# part 1
h, d = 0, 0

for line in inp:
    direction, x = line.split()
    x = int(x)
    if direction == "down":
        d += x
    elif direction == "up":
        d -= x
    else:
        h += x

print(h * d)

# part 2
h, d, aim = 0, 0, 0

for line in inp:
    direction, x = line.split()
    x = int(x)
    if direction == "down":
        aim += x
    elif direction == "up":
        aim -= x
    else:
        h += x
        d += aim * x

print(h * d)
