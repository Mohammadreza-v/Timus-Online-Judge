import sys

a, b, c = int(input()), int(input()), int(input())
n = list()

n.append(a - b * c)
n.append(a + b + c)
n.append(a * b * c)
n.append(a + b - c)
n.append(a + b * c)
n.append(a - b + c)
n.append(a - b - c)
n.append(a * b + c)
n.append(a * b - c)
n.sort()
n.reverse()

print(n.pop())

