data = [x.split("\n") for x in open("Day11.txt", "r").read().split("\n\n")]
print(data[0])
data = [[[int(y.replace(",","")) for y in x[1].split(" ")[4:]], "".join(x[2].split(" ")[-3:]), int(x[3].split(" ")[-1]), int(x[4].split(" ")[-1]), int(x[5].split(" ")[-1]),0]  for x in data]
print(data)
a = [x[2] for x in data]
total = 1
for x in a: total *=x
round = 1

while round<=10000:
    for i,x in enumerate(data):
        for old in x[0]:
            val = eval(x[1])%total
            if val%x[2]==0:
                data[x[3]][0].append(val) 
            else:
                data[x[4]][0].append(val) 
        data[i][-1] += len(x[0])
        data[i][0] = []
    round +=1
finals = sorted([x[-1] for x in data])
print(finals[-1]*finals[-2])