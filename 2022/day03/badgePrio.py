def toPrio(c):
    if ord('a') <= ord(c) <= ord('z'): # if c is lowercase
        return ord(c) - ord('a') + 1
    elif ord('A') <= ord(c) <= ord('Z'): # if c is uppercase
        return ord(c) - ord('A') + 27

f = open("input.txt", "r")
content = [line.rstrip() for line in f]
intersections = [] # list of common chars between the three Elves for each set of three Elves

for i in range(0, len(content), 3):
    intersections.append(set(content[i]).intersection(content[i+1], content[i+2]).pop())

badgeSum = 0
for c in intersections:
    badgeSum += toPrio(c)

print(badgeSum)