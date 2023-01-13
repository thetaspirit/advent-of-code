import math
f = open("input.txt", "r")
lines = f.readlines()
f.close()

P = 1

class Monkey:
    def __init__(self, items: list, operation: str, test: int, testTrue: int, testFalse: int):
        self.items = items
        self.operationString = operation
        self.test = test
        self.testTrue = testTrue
        self.testFalse = testFalse

        self.inspections = 0

    def operation(self, old):
        return eval(self.operationString)

    def testItem(self, item: int): # returns the monkey to whom the item should be thrown
        if item % self.test == 0:
            return self.testTrue
        else: return self.testFalse

    def updateInspections(self):
        self.inspections += len(self.items)

monkeys = [None for i in range(int((len(lines) + 1) / 7))]

for i in range(len(monkeys)):
    # starting items
    line = lines[1 + (i * 7)].rstrip()
    items = [int(i) for i  in line.split(": ")[1].split(",")]
    # operation
    line = lines[2 + (i * 7)].rstrip()
    operation = line.split("= ")[1]
    # test
    line = lines[3 + (i * 7)].rstrip()
    test = int(line.split()[-1])
    P *= test
    # test true
    line = lines[4 + (i * 7)].rstrip()
    testTrue = int(line.split()[-1])
    # test false
    line = lines[5 + (i * 7)].rstrip()
    testFalse = int(line.split()[-1])

    monkeys[i] = Monkey(items, operation, test, testTrue, testFalse)

for n in range(10000):
    print(n)
    for monkey in monkeys:
        monkey.updateInspections()
        for i in range(len(monkey.items)):
            item = monkey.items.pop()
            item %= P
            item = monkey.operation(item)
            # item = math.floor(item/3)
            monkeys[monkey.testItem(item)].items.append(item)

inspections = [monkey.inspections for monkey in monkeys]
print(inspections)

a = max(inspections)
inspections.remove(a)
b = max(inspections)
print(a*b)