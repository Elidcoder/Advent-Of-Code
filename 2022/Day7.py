data = [x.split(" ") for x in open("Day7.txt", "r").read().split("\n")]
from queue import LifoQueue

Path = []
directory = {}
POINTER= 0
def listGenerator():
    global POINTER
    global Path
    CD = directory
    for x in Path:
        CD = CD[x]
    while POINTER < len(data) and data[POINTER][0] != "$":
        if data[POINTER][0] != "dir":
            CD[data[POINTER][1]] = int(data[POINTER][0])
        POINTER +=1

def fileDecomposer():
    global POINTER
    global Path
    value = data[POINTER]
    POINTER +=1
    if value[0] == "$":
        if value[1] == "ls":
            return listGenerator()
        elif value[2] == "..":
            Path.pop()
        elif value[2] == "/":
            Path = []
        else: #(name)
            CD = directory
            for x in Path:
                CD = CD[x]
            Path.append(value[2])
            if value[2] not in CD:
                CD[value[2]] = {}
while POINTER < len(data):
    fileDecomposer()
values = []
def returner(a,b):
    if isinstance(a, dict):
        return totalDict(a,b)
    return a
def totalDict(dicty, key):
    total = sum([returner(dicty[x],x) for x in dicty])
    values.append(total)

    return(total)
t = 0
for x in directory:
    if isinstance(directory[x], dict):
       t +=returner(directory[x],x)
    else:
        t += directory[x]
values.append(t)

print(sum([x for x in values if x<= 100000]))

#part 2
remainder = 70000000 - t
print(t)
print(30000000-remainder)
print(min([x for x in values if x >= (30000000-remainder)]))
