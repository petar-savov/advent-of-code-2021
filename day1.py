with open("input1.txt") as f:
    inp = [int(line) for line in f.readlines()]

# part 1
count = sum([inp[i] > inp[i - 1] for i in range(1, len(inp))])
print(count)

# part 2
count = sum([inp[i] > inp[i - 3] for i in range(3, len(inp))])
print(count)
