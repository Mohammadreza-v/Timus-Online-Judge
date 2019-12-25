import sys

n = int(input())

if (n < 1 or n > 10):
    print("(1 ≤ n ≤ 10)")
    sys.exit()

Sum = float()
avg = float()
c = 0

for i in range(n):
    m = float(input())
    if (m < 3 or m > 5):
        print("(3 ≤ mi ≤ 5)")
        sys.exit()
    if (m == 3):
        c += 1
    Sum += m
if (c != 0):
    print("None")
    sys.exit()

avg = Sum / float(n)

if (avg == 5):
    print("Named")
elif (avg >= 4.5):
    print("High")
else:
    print("Common")

