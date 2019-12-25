import sys

Sum = 0
n = int(input())

if n > 10000:
    print("not greater than 10000")
    sys.exit()
if n > 0:
    for i in range(1, n + 1, 1):
        Sum = Sum + i
elif n <= 0:
    for i in range(n , 2 , 1):
        Sum = Sum + i
print(Sum)

