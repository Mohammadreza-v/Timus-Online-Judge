import sys

n = int(input())

if (n < 1 or n > 2000):
    print("(1 ≤ n ≤ 2000)")
    sys.exit()

if (n < 5):
    print("few")
elif (n < 10):
    print("several")
elif (n < 20):
    print("pack")
elif (n < 50):
    print("lots")
elif (n < 100):
    print("horde")
elif (n < 250):
    print("throng")
elif (n < 500):
    print("swarm")
elif (n < 1000):
    print("zounds")
else:
    print("legion")


