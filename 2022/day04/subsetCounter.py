def getSet(s: str):
    a = int(s.split("-")[0])
    b = int(s.split("-")[1])
    return {i for i in range(a, b+1)}

f = open("input.txt", "r")
subsets = 0

for line in f:
    line.rstrip()

    elf1 = line.split(",")[0]
    elf2 = line.split(",")[1]

    if getSet(elf1).issubset(getSet(elf2)) or getSet(elf2).issubset(getSet(elf1)):
        subsets += 1

print(subsets)