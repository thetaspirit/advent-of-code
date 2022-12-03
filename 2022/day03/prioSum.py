def toPrio(c):
    if ord('a') <= ord(c) <= ord('z'): # if c is lowercase
        return ord(c) - ord('a') + 1
    elif ord('A') <= ord(c) <= ord('Z'): # if c is uppercase
        return ord(c) - ord('A') + 27

f = open("input.txt", "r")
commonChars = [] # list of chars the two compartments have in common for each of the rucksacks

for line in f:
    string1 = line[0:len(line)//2]
    string2 = line[len(line)//2:len(line)]

    for c in string1:
        if c in string2:
            commonChars.append(c)
            break

prioSum = 0
for c in commonChars:
    prioSum += toPrio(c)

print(prioSum)

