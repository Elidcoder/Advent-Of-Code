def maklist(value):
    if not isinstance(value,list):
        return [value]
    return value
data = [(maklist(eval(x.split("\n")[0])), maklist(eval(x.split("\n")[1]))) for x in open("Day13.txt","r").read().split("\n\n")]
data = [([maklist(y) for y in x[0]], [maklist(y) for y in x[1]]) for x in data]

def correctOrder(pairvalues):
    packet1 = pairvalues[0]
    packet2 = pairvalues[1]
    for i,x in enumerate(packet1):
        if len(x) == 0:
            try:
                if len(packet2[i]) >0:
                    return True
            except:
                return False
        for j,y in enumerate(x):
            try:
                if packet1[i][j] > packet2[i][j]:
                    return False
                elif packet1[i][j] < packet2[i][j]:
                    return True
            except: return False
        if len(x)< len(packet2[i]):
            return True
    return True

packetCounted = []

for i,x in enumerate(data):
    if correctOrder(x):
        packetCounted.append(i+1)
#2789 lows
#3673 low
print(sum(packetCounted))