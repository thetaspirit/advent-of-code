def getSet(s: str):
    a = int(s.split("-")[0])
    b = int(s.split("-")[1])
    return {i for i in range(a, b+1)}

f = open("input.txt", "r")
intersections = 0

for line in f:
    line.rstrip()

    elf1 = line.split(",")[0]
    elf2 = line.split(",")[1]

    if len(getSet(elf1).intersection(getSet(elf2))) != 0:
        intersections += 1
print(intersections)