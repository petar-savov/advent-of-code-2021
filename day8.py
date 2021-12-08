with open("input8.txt") as f:
    inp = [line.strip() for line in f.readlines()]

# part 1
out = 0
for l in inp:
    line = l.split(" | ")
    for s in line[1].split():
        if len(s) in [2, 3, 4, 7]:
            out += 1

print(out)

# part 2
out = 0
for signal, output in [line.split("|") for line in inp]:
    lengths = {len(i): set(i) for i in signal.split()}
    easy = {2: "1", 3: "7", 4: "4", 7: "8"}
    n = ""
    for word in [set(i) for i in output.split()]:
        l = len(word)
        m2, m4 = len(word & lengths[2]), len(word & lengths[4])

        if l in easy:
            n += easy[l]
        if l == 5:
            if m2 == 1 and m4 == 3:
                n += "5"
            elif m2 == 2 and m4 == 3:
                n += "3"
            else:
                n += "2"
        if l == 6:
            if m2 == 1 and m4 == 3:
                n += "6"
            elif m2 == 2 and m4 == 3:
                n += "0"
            else:
                n += "9"

    out += int(n)

print(out)
