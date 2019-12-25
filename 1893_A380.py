import sys

n = input()
a = ""
Row, col = "", ""

for i in range(len(n)):
    if (n[i].isdigit()):
        Row = Row + n[i]
    else:
        col = col + n[i]

row = int(Row)

if (row <= 2):
    if(col == 'A' or col == 'D'):
        a = "window"
    else:
        a = "aisle"
    print(a)
    sys.exit()

elif (row <= 20):
    if(col == 'A' or col == 'F'):
        a = "window"
    else:
        a = "aisle"
    print(a)
    sys.exit()

else:
    if(col == 'A' or col == 'K'):
        a = "window"
    elif(col == 'C' or col == 'D' or col == 'G' or col == 'H'):
        a = "aisle"
    else:
        a = "neither"
print(a)
