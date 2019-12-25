import sys

num = int(str(input()))


def func(NUM):
    a, b, Sum, Sum1 = 0, 0, 0, 0
    n = list(str(NUM).zfill(6))
    for i in range(0, 3):
        a = int(n[i])
        b = int(n[i + 3])
        Sum = Sum + a
        Sum1 = Sum1 + b
    return (Sum == Sum1)

if (func(num+1) or func(num-1)):
    print("Yes")
else:
    print("No")
