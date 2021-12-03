from collections import Counter

with open("input3.txt") as f:
    inp = [line.strip() for line in f.readlines()]

# part 1
most, least = "", ""
for col in range(len(inp[0])):
    cnt = Counter([line[col] for line in inp])
    if cnt["1"] > cnt["0"]:
        most += "1"
        least += "0"
    else:
        most += "0"
        least += "1"

print(int(most, 2) * int(least, 2))

# part 2
ox_gen = inp.copy()
col = 0
while len(ox_gen) > 1:
    cnt = Counter([line[col] for line in ox_gen])
    most = "1" if cnt["1"] >= cnt["0"] else "0"
    ox_gen = [line for line in ox_gen if line[col] == most]
    col += 1

co2_scrubber = inp.copy()
col = 0
while len(co2_scrubber) > 1:
    cnt = Counter([line[col] for line in co2_scrubber])
    least = "1" if cnt["1"] < cnt["0"] else "0"
    co2_scrubber = [line for line in co2_scrubber if line[col] == least]
    col += 1

print(int(ox_gen[0], 2) * int(co2_scrubber[0], 2))
