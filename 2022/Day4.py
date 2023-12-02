docx = open("Day4.txt", "r").read().split("\n")
total = 0
for x in docx:
    y = x.split(",")
    a = y[0].split("-")
    b = y[1].split("-")
    firstL = set(range(int(a[0])-1))
    firstR = set(range(int(a[1])))
    secondL = set(range(int(b[0])-1))
    secondR = set(range(int(b[1])))
    overlap = (firstR-firstL) & (secondR-secondL)
    if len(overlap) !=0 : total +=1

print(total)
