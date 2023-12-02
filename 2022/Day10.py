data = open("Day10.txt", "r").read().split("\n")
counter = 0
ACC = 1
TBC = {20,60,100,140,180,220}
strng = "."*40
picture = [[x for x in strng] for z in range(6)]

scores = []

def reduce(num):
    while num>=81:
        num -=40
    return num

def check():
    if counter in TBC: scores.append(counter * ACC)
    if counter< 240:
        #print(counter, ACC, (counter%41)-1 - ACC)
        if ((reduce(counter))%41 - ACC) in [-1,1,0]: picture[int(counter/40)][reduce(counter)%41] = "#"

check()
counter +=1
check()
for x in data:
    val = x.split(" ")
    if val[0] == "noop":
        counter +=1
    else: 
        counter +=1
        check()
        counter +=1 
        ACC +=int(val[1])
    check()
print(sum(scores))

print("".join(picture[0]))
print("".join(picture[1]))
print("".join(picture[2]))
print("".join(picture[3]))
print("".join(picture[4]))
print("".join(picture[5]))
