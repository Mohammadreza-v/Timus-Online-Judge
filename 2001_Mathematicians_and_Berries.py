import sys

a1, b1 = input().split()
a2, b2 = input().split()
a3, b3 = input().split()
a1, a2, a3, b1, b2, b3,  = int(a1), int(a2), int(a3), int(b1), int(b2), int(b3)

if(a1 < 0 or a1 > 10000 or b1 < 0 or b1 > 10000 \
        or a2 < 0 or a2 > 10000 or b2 < 0 or b2 > 10000 \
        or a3 < 0 or a3 > 10000 or b3 < 0 or b3 > 10000):
    print("(0 ≤ ai, bi ≤ 10 000)")
    sys.exit()

print(a1 - a3 , b1 - b2)
