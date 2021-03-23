n = input()
ans = len(n)

if int(n)%3==0:
    print(0)
    exit()

for i in range(2**len(n)):
    num = 0
    cnt = 0
    for j in range(len(n)):
        if (i >> j) & 1:
            num += int(n[j])
            cnt += 1
    if num%3==0:
        ans = min(ans, len(n)-cnt)

if ans == len(n):
    print(-1)
else:
    print(ans)