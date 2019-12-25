n = int(input())
cnt = int(0)

for i in range(n):
    s = input()
    cnt += 1
    if("+one" in s):
        cnt += 1

cnt += 2
if(cnt == 13):
    cnt += 1

print(cnt * 100)
