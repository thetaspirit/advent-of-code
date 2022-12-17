f = open("input.txt", "r")
lines = [line.rstrip() for line in f]

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.contents = set() # contains a mix of Files and other Directories.  it's a set (as opposed to a list or smth) to account for duplicates, and idc abt order
        self.parent = parent
    
    def __repr__(self):
        if self.parent != None: # if we are not the root directory
            return repr(self.parent) + "/" + self.name
        else: return "root"

    def getSize(self):
        sum = 0
        for item in self.contents:
            if isinstance(item, File):
                sum += item.size
            elif isinstance(item, Directory):
                sum += item.getSize()
        return sum

    def tree(self, indent=0): # uese rEeeeEEEeeEcUrsIoN to PRINT a lil file tree
        i = indent
        # first print the name of this directory
        print(("| " * i) + self.name + " (dir)")
        for item in self.contents:
            if isinstance(item, Directory):
                item.tree(indent=i+1)
            elif isinstance(item, File):
                print((("| ") * (i + 1)) + item.name + " " + str(item.size))


class File:
    def __init__(self, name, size, parent: Directory):
        self.name = name
        self.size = size
        self.parent = parent
    def __repr__(self):
        return str(self.parent) + "/" + self.name

def findChildDir(name, parent: Directory): # returns a Directory with given name in parent Directory.  Returns None if none found
    for item in parent.contents:
        if isinstance(item, Directory):
            if item.name == name:
                return item
    return None

root = Directory("/", None)
currentDir = root
dirs = set() # set of all directories and subdirectories so we can calculate their sum later.  doesn't matter if we add same object multipl times :)

i = 1 # yes, that's a 1 not a 0 hahaaaaaaaaaaaaaaaaaa (we're skipping the first line bc it's always "cd /")
while i < len(lines):
    dirs.add(currentDir)

    line = lines[i]
    if line[0] == "$":
        command = line.split()[1]

        if command == "cd":
            dirName = line.split()[2]

            if dirName != "..":
                # Check if the Directory we are cd-ing into already exists as a child
                if findChildDir(dirName, currentDir) == None: # if not, create it
                    currentDir = Directory(dirName, currentDir)
                    currentDir.parent.contents.add(currentDir) # also add the new directory to its parent's self.contents
                else: # otherwise, set that pre-existing Directory as our current
                    currentDir = findChildDir(dirName, currentDir) 

            else: # we are cd-ing upward
                currentDir = currentDir.parent
                i += 1
                continue

        if command == "ls":
            i += 1
            continue

    if line[0] != "$":
        if line.split()[0] != "dir": # add the file size and name to our list of current Directory's contents
            currentDir.contents.add(File(line.split()[1], int(line.split()[0]), currentDir))
    
    i += 1

total = 0

for d in dirs:
    s = d.getSize()
    if s <= 100000:
        total += s

print(total)