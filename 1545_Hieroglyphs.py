import sys

n = int(input())

if (n < 1 or n > 1000):
    print("(1 ≤ N ≤ 1000)")
    sys.exit()

c = list()

for i in range(0, n):
    s = input()
    c.append(s)

a = input()

for i in range(0, n):
    if(c[i][0] == a):
        print(c[i])
