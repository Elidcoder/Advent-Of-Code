data =  [[int(y) for y in x] for x in open("Day8.txt", "r").read().split("\n")]
for x in range(len(data)):
    data[x].insert(0,-1)
    data[x].append(-1)

data.insert(0,[-1 for x in range(len(data[0]))])
data.append([-1 for x in range(len(data[0]))])
maxLR = [[max(x[:y+1]) for y in range(len(x))] for x in data]
maxRL = [[max(x[-y-1:]) for y in range(len(x))][::-1] for x in data]

maxTB = [[max([data[z][y] for z in range(x+1)]) for y in range(len(data[x]))] for x in range(len(data))]
revData = data.copy()[::-1]
maxBT = [[max([revData[z][y] for z in range(x+1)]) for y in range(len(revData[x]))] for x in range(len(data))][::-1]
total = 0
for i,x in enumerate(data[1:-1]):
    for j,y in enumerate(x[1:-1]):
        val = data[i+1][j+1]
        if maxTB[i][j+1]<val or maxBT[i+2][j+1]<val or maxRL[i+1][j+2]<val or maxLR[i+1][j]<val:
            total +=1
print(total)
startval = 0
for y,row in enumerate(data[1:-1]):
    y+=1
    for x,tree in enumerate(row[1:-1]):
        x+=1
        a = 0
        r1 = True
        #up
        while r1:
            if data[y-a-1][x] == -1: r1 = False
            else: a +=1
            if data[y-a][x] >= tree:
                r1 = False

        #left
        c = 0
        r3 = True
        while r3:
            if data[y][x-c-1] == -1: r3 = False
            else: c+=1
            if data[y][x-c] >= tree:
                r3 = False
        #down
        b = 0
        r2 = True
        while r2:
            if  data[y+b+1][x] == -1: r2 = False
            else:b+=1
            if data[y+b][x] >= tree:
                r2 = False
        #right
        d = 0
        r4 = True
        while r4:
            if  data[y][x+d+1] == -1: r4 = False
            else: d+=1
            if data[y][x+d] >= tree:
                r4 = False
        startval = max(startval,a*b*c*d)
print(startval)