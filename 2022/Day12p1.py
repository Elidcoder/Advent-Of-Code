data = [[y for y in x]for x in open("Day12.txt","r").read().split("\n")]
width = len(data[0])
height = len(data)
visited = set()

for i,x in enumerate(data):
    try: 
        ex = x.index("S")
        curpos = (ex,i,ord("a")-96)
    except: pass
visited.add((curpos[0],curpos[1]))
data[curpos[1]][curpos[0]] = "a"
curpos = {curpos,}
for i,x in enumerate(data):
    try: 
        ex = x.index("E")
        finpos = (ex,i)
    except: pass
data[finpos[1]][finpos[0]] = "z"
data = [[ord(y)-96 for y in x]for x in data]

print("final:",finpos)
counter = 0
done =False
while done == False:
    counter +=1
    temp = set()
    for z in curpos:
        neighbours = {(z[0]+1,z[1]),(z[0]-1,z[1]),(z[0],z[1]+1),(z[0],z[1]-1)}
        neighbours = neighbours - visited 
        if z[0] == width-1:
            neighbours.remove((z[0]+1,z[1]))
        elif z[0] == 0 :
            neighbours.remove((z[0]-1,z[1]))
        if z[1] == 0 :
            neighbours.remove((z[0],z[1]-1))
        elif z[1] == height-1:
            neighbours.remove((z[0],z[1]+1))
        for x in neighbours:
            if data[x[1]][x[0]]-1<= z[2]:

                if (x[0],x[1])==finpos:
                    done = True

                visited.add((x[0],x[1]))
                temp.add((x[0],x[1],data[x[1]][x[0]]))
    
    curpos = temp.copy()
    

    
print(counter)