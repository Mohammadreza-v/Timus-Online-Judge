import sys

n, m, y = input().split()
n, m, y = int(n), int(m), int(y)
i = list()

if (n <= 0 or n >= 999 or m <= 1 or m >= 999 or y <= 0 or y >= 999):
    print("0 < N < 999, 1 < M < 999, 0 < Y < 999")
    sys.exit()
for x in range(0, int(m)):
    if ((x ** n) % m == y):
        i.append(x)
        i.sort()

a = len(i)
if(a == 0):
    print(int('-1'), end=' ')
for v in range(0, a):
    print(int(i[v]), end=' ')
